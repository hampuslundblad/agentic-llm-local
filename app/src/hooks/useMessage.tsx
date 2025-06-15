import { useMutation } from "@tanstack/react-query"
import { Api } from "@/api/api"

export const useMessage = () => {
  return useMutation({
    mutationFn: (message:string) => Api.postMessage(message),    
    retry: 1,
  })
}
