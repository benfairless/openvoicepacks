"""Tests for the TTS provider classes."""

import boto3
import botocore.exceptions
import pytest

import openvoicepacks.providers


class TestProvider:
    """Test suite for the base Provider class."""

    def test_provider_process_not_implemented(self, tmp_path) -> None:
        """Provider.process() should raise NotImplementedError if not overridden."""
        provider = openvoicepacks.providers.Provider()
        with pytest.raises(NotImplementedError):
            provider.process(str(tmp_path / "dummy.wav"), "text")

    def test_provider_raises_invalid_string(self) -> None:
        """Given an invalid provider name, an error is raised."""
        provider = openvoicepacks.providers.Provider()
        with pytest.raises(NotImplementedError):
            provider.generate("Test Provider is Invalid")


class TestPiper:
    def test_piper_process_writes_wav(self, client, tmp_path) -> None:
        """Piper.process() should write a valid wav file to the given path."""
        out_path = tmp_path / "test.wav"
        client.process(str(out_path), "Test Piper Process is Valid")
        assert out_path.exists(), "WAV file was not created."
    """Test suite for the Piper TTS provider."""

    @pytest.fixture
    def client(self) -> openvoicepacks.providers.Piper:
        """Return a Piper client instance."""
        return openvoicepacks.providers.Piper()

    @pytest.fixture
    def client_tmp(self, tmp_path) -> openvoicepacks.providers.Piper:
        """Return a Piper client instance with a temporary install directory."""
        return openvoicepacks.providers.Piper(install_dir=tmp_path)

    def test_piper_processes_valid_string(self, client) -> None:
        """Given a valid string, Piper is able to process the request."""
        assert isinstance(
            client.generate("Test Piper Process is Valid"),
            openvoicepacks.audio.TXSoundData,
        ), "Audio data is not a valid TXSoundData object."

    @pytest.mark.slow
    def test_piper_on_fresh_install(self, tmp_path) -> None:
        """Given a fresh install, Piper downloads model and processes the request."""
        client = openvoicepacks.providers.Piper(install_dir=tmp_path)
        assert isinstance(
            client.generate("Test Piper Process on Fresh Install"),
            openvoicepacks.audio.TXSoundData,
        ), "Audio data is not a valid TXSoundData object."

    @pytest.mark.slow
    def test_piper_downloads_voice_model(self, client_tmp) -> None:
        """Given a valid voice model ID, Piper downloads voice model successfully."""
        model_id = "en_GB-alan-medium"
        model_path = client_tmp.install_dir / f"{model_id}.onnx"
        client_tmp.download_voice(model_id)
        assert model_path.exists(), "Voice model was not downloaded successfully."

    def test_piper_download_raises_invalid_string(self, client_tmp) -> None:
        """Given an invalid voice model ID, an error is raised."""
        model_id = "en_GB-invalid-medium"
        with pytest.raises(
            openvoicepacks.providers.ProviderError, match="Not available"
        ):
            client_tmp.download_voice(model_id)


class TestPolly:
    """Test suite for the Polly TTS provider"""

    def test_polly_process_writes_wav(self, client, tmp_path) -> None:
        """Polly.process() should write a valid wav file to the given path."""
        out_path = tmp_path / "test.wav"
        client.process(str(out_path), "Test Polly Process is Valid")
        assert out_path.exists(), "WAV file was not created."

    @pytest.fixture
    def client(self) -> openvoicepacks.providers.Polly:
        """Return a Polly client instance."""
        return openvoicepacks.providers.Polly()

    def test_polly_with_invalid_session(self) -> None:
        """Given invalid AWS credentials, an error is raised."""
        session = boto3.session.Session(
            aws_access_key_id="invalid",
            aws_secret_access_key="invalid",
            aws_session_token="invalid",
        )
        with pytest.raises(
            (botocore.exceptions.NoCredentialsError, botocore.exceptions.ClientError),
        ):
            openvoicepacks.providers.Polly(session=session)

    def test_polly_with_valid_session(self) -> None:
        """Given valid AWS credentials, a Polly client is created successfully."""
        assert isinstance(
            openvoicepacks.providers.Polly(), openvoicepacks.providers.Polly
        ), "Polly client was not created successfully."

    def test_polly_processes_valid_string(self, client) -> None:
        """Given a valid string, AWS Polly is able to process the request."""
        assert isinstance(
            client.generate("Test Polly Process is Valid"),
            openvoicepacks.audio.TXSoundData,
        ), "Audio data is not a valid TXSoundData object."

    def test_polly_raises_invalid_string(self, client) -> None:
        """Given an invalid string, an error is raised."""
        with pytest.raises(
            (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError),
        ):
            client.generate("<ssml_invalid_tag>")
