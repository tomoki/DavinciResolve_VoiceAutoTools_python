class VoiceMediaBin:

    def __init__(self, resolve, voice_outputbin):
        self.resolve = resolve
        self.mediapool = self._getMediapool(resolve)
        self.bin = self._getBin(self.mediapool, voice_outputbin)

    def PullVoiceToAudioMediaBin(self, voice_file_path: str):
        self.resolve \
            .GetProjectManager() \
            .GetCurrentProject() \
            .GetMediaPool() \
            .SetCurrentFolder(self.bin)

        storage = self.resolve.GetMediaStorage()
        clip_list = storage.AddItemListToMediaPool(voice_file_path)

        return clip_list

    #def PullAllVoiceToAudioMediaBin(self, resolve, voice_folder_path: str):
    #    # 同じかんじ
    #    resolve \
    #        .GetProjectManager() \
    #        .GetCurrentProject() \
    #        .GetMediaPool() \
    #        .SetCurrentFolder(self.bin)

    #    storage = resolve.GetMediaStorage()
    #    storage.AddItemListToMediaPool(voice_folder_path)
    #    # 全部もってくる、ファイル更新順

    #    pass

    def putVoice2Timeline(self, voice_mediapoolitem):
        timelineitem_list = self.mediapool.AppendToTimeline(voice_mediapoolitem)
        return timelineitem_list

    def _getMediapool(self, resolve):
        mediapool = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetMediaPool()
        return mediapool

    def _getBin(self, mediapool, voice_outputbin):
        root_bin = mediapool.GetRootFolder()

        sub_folders = root_bin.GetSubFolderList()
        for folder in sub_folders:
            if(folder.GetName() == voice_outputbin):
                return folder

        return mediapool.AddSubFolder(root_bin, voice_outputbin)