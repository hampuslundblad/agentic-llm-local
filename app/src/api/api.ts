export const Api = {
  postMessage: async (message: string) : Promise<{message: string}> => {
    const response = await fetch(
      `http://localhost:5173/api/message`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ content: message }),
      },
    )
    if (!response.ok) {
      throw new Error(
        `Error fetching post with id ${message}: ${response.statusText}`,
      )
    }
    return response.json()
  },
}
