const sendMessage = async () => {
  try {
    console.log("Sending request...");

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: query,
        user_type: "admin",
      }),
    });

    console.log("Response status:", res.status);

    const data = await res.json();
    console.log("Data:", data);

    setMessages((prev) => [
      ...prev,
      { role: "user", text: query },
      { role: "ai", text: data.response },
    ]);

    setQuery("");
  } catch (err) {
    console.error("ERROR:", err);
  }
};