class AudioHack.Models
    @Annotation:
        Backbone.Model.extend
            
    @Annotations:
        Backbone.Collection.extend
            model: @Annotation,
            urlRoot: '/'