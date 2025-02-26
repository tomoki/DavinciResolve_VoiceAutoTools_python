import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from Domain.VoiceMediaBin import VoiceMediaBin

class VoiceSyncWoeker:

    class VoiceSyncEventHandler(LoggingEventHandler):
        def __init__(self, voice_media_bin):

            super().__init__()
            self.voice_media_bin = voice_media_bin

        def on_created(self, event):
            # ファイル置かれた直後だと偶にバグるのでWait挟む
            time.sleep(0.5)
            filepath = event.src_path
            item = self.voice_media_bin.PullVoiceToAudioMediaBin(filepath)
            self.voice_media_bin.putVoice2Timeline(item)

    def __init__(self, resolve, voice_outputbin, folder_path) -> None:
        self.resolve = resolve
        self.folder_path = folder_path
        self.voice_media_bin = VoiceMediaBin(resolve, voice_outputbin)
        self.event_handler = self.VoiceSyncEventHandler(self.voice_media_bin)

    def SyncerExecute(self):
        self.observer = Observer()

        self.observer.schedule(
            self.event_handler,
            self.folder_path,
            recursive=False
            )
        self.observer.start()

    def SyncerStop(self):
        self.observer.stop()
        self.observer.join()
        
