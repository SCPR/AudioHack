class AudioHack.Player
    DefaultOptions:
        assetBrowserEl: "#asset_browser"
        modalSelect: true
        modalAdmin: true            

    constructor: (options) ->
        @options = _(_({}).extend(this.DefaultOptions)).extend( options || {} )
        