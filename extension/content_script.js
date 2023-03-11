console.log("Discord presence is on")

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log(message)
    return true
});
