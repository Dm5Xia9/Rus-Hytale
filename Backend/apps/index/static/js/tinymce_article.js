tinymce.init({
  selector: '#mytextarea',
  menubar: 'edit insert format table tools help',
  height: '500px',
  language: 'ru',
  plugins: " advlist,autoresize, autolink,lists,link,image,charmap,print,preview,anchor,searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,code,wordcount",
  autoresize_on_init: true,
  image_title: true,
  nowrap : false,
  image_class_list: [
    {title: 'image', value: 'img_public'},
    ],
  object_resizing : false,
  images_upload_url: '/articles/file/',
  images_dataimg_filter: function(img) {
    return !img.hasAttribute('internal-blob');
  },
  automatic_uploads: true,
  file_picker_types: 'image',
  init_instance_callback: function (inst) { inst.execCommand('mceAutoResize'); },
  file_picker_callback: function (cb, value, meta) {
    var input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');
    var filename = "";
    input.onchange = function () {
      var file = this.files[0];
      var fd = new FormData;
      fd.append('file', file);
      $.ajax(
      {
        type:"POST",
        dataType: 'json',
        url: "/articles/file/",
        data: fd,
        processData: false,
        contentType: false,
        success: function(data) {
          console.log(data);
          filename = data.location;
          cb(filename, {width:"100%", height:""});}
  })};

    input.click();
  },
  skin_url: "/static/css/custom/ui/CUSTOM",
  toolbar: 'redo undo forecolor backcolor bold italic strikethrough underline subscript superscript fontselect fontsizeselect alignjustify alignleft aligncenter alignright blockquote indent lineheight outdent',
  max_height: 500
});
