AudioHack ?= {}

class AudioHack.Base
    DefaultOptions:
        assetBrowserEl: "#asset_browser"
        modalSelect: true
        modalAdmin: true            

    constructor: (data,options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )

        @annotations = new AudioHack.Models.Annotations data.annotations||[]    
    
        console.log "init player with ", data.soundcloud_id
        @player = new AudioHack.Player
            soundcloudFileId: data.soundcloud_id
            
        @player.bind "timeupdate", => @annotations.tick @player.popcorn.currentTime()
        #@player.bind "timeupdate", => console.log "tickTock", @player.popcorn.currentTime()
        
        @aView = new AudioHack.Models.AnnotationsView collection:@annotations
        $("#annotations").html @aView.el

        