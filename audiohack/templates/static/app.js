(function() {
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  if (typeof AudioHack === "undefined" || AudioHack === null) {
    AudioHack = {};
  }
  AudioHack.Base = (function() {
    Base.prototype.DefaultOptions = {
      assetBrowserEl: "#asset_browser",
      modalSelect: true,
      modalAdmin: true
    };
    function Base(data, options) {
      this.options = _(_({}).extend(this.DefaultOptions)).extend(options || {});
      this.player = new Player({
        soundcloudFileId: this.data.soundcloud_id
      });
      this.annotations = new Models.Annotations(data.annotations || []);
      this.player.bind("timeupdate", __bind(function(tick) {
        return this.annotations.tick(tick);
      }, this));
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
      soundcloudClientId: "74186e4ab0b72e1d480f4b5e147042fb",
      soundcloudFileId: "",
      htmlDiv: "player"
    };
    function Player(options) {
      this.options = _(_({}).extend(this.DefaultOptions)).extend(options || {});
      console.log("init for soundcloud on ", this.options.soundcloudFileId);
      this.popcorn = Popcorn(Popcorn.soundcloud(this.options.htmlDiv, this.options.soundcloudFileId, {
        api: {
          key: this.options.soundcloudClientId
        }
      }));
    }
    return Player;
  })();
}).call(this);
