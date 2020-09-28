/** @type {WindowProxy} */ let cameraWindow = null;
let captureData = null;

function openCameraWindow() {
    cameraWindow = window.open("camera.html", "xtremettt_camera", "innerWidth=800,innerHeight=600");
}

function isCameraCaptured() {
    return cameraWindow == null;
}

function getCaptureData() {
    return captureData;
}

function cancelCameraCapture() {
    if (cameraWindow != null) {
        cameraWindow.close();
    }
}

function setCaptureData(data) {
    captureData = data;
    cameraWindow = null;
}
