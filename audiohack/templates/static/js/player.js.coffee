class AudioHack.Player
    DefaultOptions:
        soundcloudClientId: "74186e4ab0b72e1d480f4b5e147042fb"
        soundcloudFileId: ""
        htmlDiv: "player"

    constructor: (options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
        
        @popcorn = Popcorn( Popcorn.soundcloud( @options.htmlDiv, @options.soundcloudFileId, {
          api: {
            key: @options.soundcloudClientId,
          }
        }) );
