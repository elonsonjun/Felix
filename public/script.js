async function sendQuery() {
  const query = document.getElementById("query").value;
  const res = await fetch("/api/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });
  const data = await res.json();
  document.getElementById("response").textContent = data.response;
}

async function sendTeamQuery() {
  const query = document.getElementById("query").value;
  const res = await fetch("/api/team", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });
  const data = await res.json();
  document.getElementById("response").textContent = data.response;
}