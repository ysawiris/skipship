chrome.runtime.onInstalled.addListener(function() {
    console.log("testing");
    chrome.storage.sync.set({ color: '#3aa757' }, function() {
        console.log("The color is green.");
    });
});

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    console.log("Listening")
    if (changeInfo.url !== "undefined" && changeInfo.url !== undefined) {
        let url = changeInfo.url.toString();
        if (url.includes("/dp/")) {
            console.log("show pop up");
            let title = document.getElementById('productTitle');
            console.log(title);
            chrome.tabs.executeScript({ code: 'document.body.style.backgroundColor="orange"' });
        }
        console.log('Tab %d got new URL: %s', tabId, changeInfo.url);
    }
});