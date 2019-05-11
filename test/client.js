var socket = io.connect('http://localhost:5000')
var canvas = document.querySelector('canvas#cam')
var video = document.querySelector('#video')
setInterval(function () {
  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
      video: true
    })
      .then(function (stream) {
        video.srcObject = stream
        const track = stream.getVideoTracks()[0]
        let imageCapture = new ImageCapture(track)
        imageCapture.grabFrame()
          .then(function (imageBitmap) {
              // console.log('Grabbed frame:', imageBitmap);
            canvas.getContext('2d').drawImage(imageBitmap, 0, 0)
          })
      })
      .catch(function (error) {
        console.log(error)
      })
  }
  var url = canvas.toDataURL()
  // console.log(url);
  socket.emit('frame', url)
}, 100)
var processed = document.querySelector('canvas#res')
socket.on('processed', function (imageURI) { // processed frame
  var ctx = processed.getContext('2d')
  var img = new Image()
  img.onload = function () {
    ctx.drawImage(img, 0, 0)
  }
  img.src = imageURI
})
