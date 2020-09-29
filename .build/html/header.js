/** @type {WindowProxy} */ let cameraWindow = null;
/** @type {Uint8Array} */ let captureData = null;

function openCameraWindow() {
    cameraWindow = window.open("camera.html", "xtremettt_camera", "innerWidth=800,innerHeight=600");
}

function isCameraCaptured() {
    return cameraWindow == null;
}

function cancelCameraCapture() {
    if (cameraWindow != null) {
        cameraWindow.close();
    }
}

function setCaptureData(/** @type {ArrayBuffer} */ data) {
    captureData = new Uint8Array(data);
    cameraWindow = null;
}
