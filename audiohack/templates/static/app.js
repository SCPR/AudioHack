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
      this.annotations = new AudioHack.Models.Annotations(data.annotations || []);
      console.log("init player with ", data.soundcloud_id);
      this.player = new AudioHack.Player({
        soundcloudFileId: data.soundcloud_id
      });
      this.player.bind("timeupdate", __bind(function() {
        return this.annotations.tick(this.player.popcorn.currentTime());
      }, this));
      this.player.bind("timeupdate", __bind(function() {
        return $("#time").html(this.player.popcorn.currentTime());
      }, this));
      this.aView = new AudioHack.Models.AnnotationsView({
        collection: this.annotations
      });
      $("#annotations").html(this.aView.el);
    }
    return Base;
  })();
  AudioHack.Models = (function() {
    function Models() {}
    Models.Annotation = Backbone.Model.extend({
      url: "/"
    });
    Models.Annotations = Backbone.Collection.extend({
      model: Models.Annotation,
      tick: function(time) {
        this.each(__bind(function(a) {
          if (a.get("start") < time && a.get("end") > time) {
            return a.set({
              VISIBLE: true
            });
          } else {
            return a.set({
              VISIBLE: false
            });
          }
        }, this));
        return true;
      }
    });
    Models.AnnotationView = Backbone.View.extend({
      tagName: "li",
      template: "Annotation: <%= description %>",
      initialize: function() {
        console.log("init view for ", this.model);
        return this.model.bind("change", __bind(function() {
          console.log("change for ", this.model);
          return this.render();
        }, this));
      },
      render: function() {
        if (this.model.get("VISIBLE") === true) {
          $(this.el).html(_.template(this.template, this.model.toJSON()));
        } else {
          $(this.el).html('');
        }
        return this;
      }
    });
    Models.AnnotationsView = Backbone.View.extend({
      tagName: 'ul',
      initialize: function() {
        this._views = {};
        this.collection.bind('add', __bind(function(f) {
          console.log("add event from ", f);
          this._views[f.cid] = new Models.AnnotationView({
            model: f
          });
          return this.render();
        }, this));
        this.collection.bind('remove', __bind(function(f) {
          console.log("remove event from ", f);
          $(this._views[f.cid].el).detach();
          delete this._views[f.cid];
          return this.render();
        }, this));
        this.collection.bind('reset', __bind(function(f) {
          console.log("reset event from ", f);
          return this._views = {};
        }, this));
        return this.render();
      },
      render: function() {
        this.collection.each(__bind(function(f) {
          var _base, _name, _ref;
          return (_ref = (_base = this._views)[_name = f.cid]) != null ? _ref : _base[_name] = new Models.AnnotationView({
            model: f
          });
        }, this));
        $(this.el).append(_(this._views).map(function(v) {
          return v.el;
        }));
        return this;
      }
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
        this.popcorn.pause();
        this.popcorn.play();
        console.log("popcorn is ", this.popcorn);
        return this.popcorn.listen("timeupdate", __bind(function(evt) {
          return this.trigger('timeupdate', evt);
        }, this));
      }, this));
    }
    return Player;
  })();
}).call(this);
