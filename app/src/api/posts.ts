export const Post = {
  getById: async (id: string) => {
    console.log(`Fetching post with id: ${id}`)
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${id}`,
    )
    if (!response.ok) {
      throw new Error(
        `Error fetching post with id ${id}: ${response.statusText}`,
      )
    }
    return response.json()
  },
}
