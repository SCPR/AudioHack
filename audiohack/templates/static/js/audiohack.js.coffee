AudioHack ?= {}

class AudioHack.Base
    DefaultOptions:
        assetBrowserEl: "#asset_browser"
        modalSelect: true
        modalAdmin: true            

    constructor: (data,options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
    
        console.log "init player with ", data.soundcloud_id
        @player = new AudioHack.Player
            soundcloudFileId: data.soundcloud_id
            
        @annotations = new AudioHack.Models.Annotations data.annotations||[]    
        #@player.bind "timeupdate", (tick) => @annotations.tick tick
        
        @player.bind "timeupdate", (evt) => console.log "tick is ", evt
        