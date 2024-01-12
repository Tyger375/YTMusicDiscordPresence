webRequest.onBeforeRequest.addListener(
        function(details) {
            //return {cancel: details.url.indexOf("://music.youtube.com/") != -1};
            let cookies = ""
            let url = details.url;
            if (url.includes("next"))
                request("")
            else if (url.includes("watchtime"))
            {
                if (url.includes("paused"))
                    request("pause")
                else if (url.includes("playing"))
                    request("resume")
            }
        },
    { urls: ["<all_urls>"] }
);


function request(action) {
    fetch("http://127.0.0.1:5000/" + action,
          {
              method: "POST",
              headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
              }
          })
}