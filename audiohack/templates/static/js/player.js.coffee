class AudioHack.Player
    DefaultOptions:
        soundcloudClientId: "74186e4ab0b72e1d480f4b5e147042fb"
        soundcloudFileId: ""
        htmlDiv: "player"

    constructor: (options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
        
        # add in events
        _.extend(this, Backbone.Events)
        
        console.log "init for soundcloud on ", @options.soundcloudFileId
        
        $ =>        
            @popcorn = Popcorn( Popcorn.soundcloud( @options.htmlDiv, @options.soundcloudFileId, {
              api: {
                key: @options.soundcloudClientId,
              }
            }) );
            
            @popcorn.pause()
            @popcorn.play()
            
            console.log "popcorn is ", @popcorn
            
            @popcorn.listen "timeupdate", (evt) => @trigger 'timeupdate', evt
        