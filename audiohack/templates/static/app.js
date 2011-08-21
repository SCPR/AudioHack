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
      console.log("init player with ", data.soundcloud_id);
      this.player = new AudioHack.Player({
        soundcloudFileId: data.soundcloud_id
      });
      this.annotations = new AudioHack.Models.Annotations(data.annotations || []);
      this.player.bind("timeupdate", __bind(function(evt) {
        return console.log("tick is ", this.player.popcorn.currentTime());
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
      _.extend(this, Backbone.Events);
      console.log("init for soundcloud on ", this.options.soundcloudFileId);
      $(__bind(function() {
        this.popcorn = Popcorn(Popcorn.soundcloud(this.options.htmlDiv, this.options.soundcloudFileId, {
          api: {
            key: this.options.soundcloudClientId
          }
        }));
        return this.popcorn.listen("load", __bind(function() {
          this.popcorn.play();
          console.log("popcorn is ", this.popcorn);
          return this.popcorn.listen("timeupdate", __bind(function(evt) {
            return this.trigger('timeupdate', evt);
          }, this));
        }, this));
      }, this));
    }
    return Player;
  })();
}).call(this);
