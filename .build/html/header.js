let captureFinished = false;
let captureData = null;

function openCameraWindow() {
    captureFinished = false;
    window.open("camera.html", "xtremettt_camera", "innerWidth=800,innerHeight=600");
}

function setCaptureData(data) {
    captureData = data;
    captureFinished = true;
}
