AudioHack ?= {}

class AudioHack.Base
    DefaultOptions:
        assetBrowserEl: "#asset_browser"
        modalSelect: true
        modalAdmin: true            

    constructor: (data,options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
    
        @player = new Player
            soundcloudFileId: @data.soundcloud_id
            
        @annotations = new Models.Annotations(data.annotations||[])    
        @player.bind "timeupdate", (tick) => @annotations.tick tick
        
        