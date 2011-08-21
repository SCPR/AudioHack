(function() {
  if (typeof AudioHack === "undefined" || AudioHack === null) {
    AudioHack = {};
  }
  AudioHack.Base = (function() {
    Base.prototype.DefaultOptions = {
      assetBrowserEl: "#asset_browser",
      modalSelect: true,
      modalAdmin: true
    };
    function Base(options) {
      this.options = _(_({}).extend(this.DefaultOptions)).extend(options || {});
      this.player = new Player();
    }
    return Base;
  })();
  AudioHack.Models = (function() {
    function Models() {}
    Models.Annotation = Backbone.Model.extend;
    Models.Annotations = Backbone.Collection.extend({
      model: Models.Annotation,
      urlRoot: '/'
    });
    return Models;
  })();
  AudioHack.Player = (function() {
    Player.prototype.DefaultOptions = {
      assetBrowserEl: "#asset_browser",
      modalSelect: true,
      modalAdmin: true
    };
    function Player(options) {
      this.options = _(_({}).extend(this.DefaultOptions)).extend(options || {});
    }
    return Player;
  })();
}).call(this);
