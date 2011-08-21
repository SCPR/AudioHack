class AudioHack.Models
    @Annotation:
        Backbone.Model.extend
            url: "/"
            
    @Annotations:
        Backbone.Collection.extend
            model: @Annotation,
            
            tick: (time) ->
                @.each (a) => 
                    if a.get("start") < time && a.get("end") > time
                        a.set VISIBLE: true
                    else
                        a.set VISIBLE: false
                        
                true
                        
    @AnnotationView:
        Backbone.View.extend
            tagName: "li"
            
            template:
                """
                Annotation: <%= description %>
                """
                
            initialize: ->
                console.log "init view for ", @model
                @model.bind "change", => console.log("change for ",@model);@render()
                
            render: ->
                if @model.get("VISIBLE") == true
                    $( @el ).html _.template @template, @model.toJSON()
                else
                    $( @el ).html('')
                    
                this
                
    @ImageView:
        @AnnotationView.extend
            template:
                """
                <img src="<%= url %>"/>
                """
                
    @ViewMap:
        "TEXT": "AnnotationView",
        "IMAGE": "ImageView"
                        
    @AnnotationsView:
        Backbone.View.extend
            tagName: 'ul'
            
            initialize: ->
                @_views = {}

                @collection.bind 'add', (f) => 
                    console.log "add event from ", f
                    @_views[f.cid] = new Models[Models.ViewMap[f.get("type")||"AnnotationView"]]({model:f})
                    @render()

                @collection.bind 'remove', (f) => 
                    console.log "remove event from ", f
                    $(@_views[f.cid].el).detach()
                    delete @_views[f.cid]
                    @render()

                @collection.bind 'reset', (f) => 
                    console.log "reset event from ", f
                    @_views = {}
                    
                @render()
                
            render: ->
                # set up views for each collection member
                @collection.each (f) => 
                    # create a view unless one exists
                    @_views[f.cid] ?= new Models[Models.ViewMap[f.get("type")||"AnnotationView"]]({model:f})

                # make sure all of our view elements are added
                $(@el).append( _(@_views).map (v) -> v.el )
                
                @