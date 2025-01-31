function filterRequests(status) {
    fetch(`/api/requests?status=${status}`)
        .then(response => response.json())
        .then(data => updateTable(data));
}