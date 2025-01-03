from .BcutASR import BcutASR
from .JianYingASR import JianYingASR
from .KuaiShouASR import KuaiShouASR
from .WhisperASR import WhisperASR
from .WhisperAPI import WhisperAPI

__all__ = ["BcutASR", "JianYingASR", "KuaiShouASR", "WhisperASR", "WhisperAPI"]


def transcribe(audio_file, platform):
    assert platform in __all__
    asr = globals()[platform](audio_file)
    return asr.run()
