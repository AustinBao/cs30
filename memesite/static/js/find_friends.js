let friend_input = document.getElementById("friends_search")

friend_input.addEventListener("keydown",  function(event) {
    if (event.key === "Enter") {
        send_username(); //
    }
});



function send_username() {
    // get value of input
    let username = friend_input.value;
    console.log(`/friends/${username}`);

    fetch(`/friends/?username=${username}`, { method:'GET' })
      .then(response => {
        history.pushState({}, '', `/friends/?username=${username}`);
        return response;
      })
      .then(data => {
        if (data) {
            console.log("Sent friend username:", username);
            location.reload();
        } else {
            console.error("Failed to send friend username:", username);
        }
      })
      .catch(error => console.log(error))
}
