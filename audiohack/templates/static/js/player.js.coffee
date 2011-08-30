class AudioHack.Player
    DefaultOptions:
        audio_url: ""
        htmlDiv: "#player"

    constructor: (options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
        
        # add in events
        _.extend(this, Backbone.Events)
        
        console.log "init for player on ", @options.audio_url
        
        @jplayer = $(@options.htmlDiv).jPlayer
            supplied: 'mp3'
            solution: 'html'
            autoplay: 'metadata'
            ready: (evt) => 
                console.log "in ready evt for jPlayer"
                $(@options.htmlDiv).jPlayer "setMedia", 
                    mp3: @options.audio_url
                    @popcorn = Popcorn "#" + @jplayer.data('jPlayer').internal.audio.id 
                    
                    @popcorn.listen "timeupdate", (evt) => @trigger 'timeupdate', evt
