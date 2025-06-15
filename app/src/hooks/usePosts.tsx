import { useQuery } from "@tanstack/react-query"
import { Post } from "@/api/posts"

export const usePosts = (id: string) => {
  return useQuery({
    queryKey: ["posts", id],
    queryFn: () => Post.getById(id),
    staleTime: 1000 * 60 * 5, // 5 minutes
    retry: 1,
    enabled: !!id, // Only run the query if id is truthy
  })
}
