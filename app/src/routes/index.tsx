import  { useEffect, useState } from "react"
import { createFileRoute } from "@tanstack/react-router"
import ChatMessage from "@/components/ChatMesssage"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { useMessage } from "@/hooks/useMessage"
import ChatMessageLoading from "@/components/ChatMessageLoading"

export const Route = createFileRoute("/")({
  component: App,
})

type Message = {
  message: string;
  type: "sent" | "received";
}

function App() {
  const postMessage = useMessage();
  const [input, setInput] = useState("")
  const [messages, setMessages] = useState<Array<Message>>([])
  console.log("postMessage", postMessage.data)

  const handleSend = () => {
    if (input.trim() === "") return
    // Call the API to post the message
    postMessage.mutate(input);
    setMessages((prev) => [ ...prev, { message: input, type: "sent" }])
    setInput("")
  }
  console.log("messages", messages)
  useEffect(() => {
    if (postMessage.isSuccess) {
      setMessages((prev) => [ ...prev, { message: postMessage.data.message, type: "received" }])
    }
  }, [postMessage.isSuccess, postMessage.data])


  return (
    <div className="flex flex-col w-1/2 m-auto">
      <div className="space-y-2 mb-4">
     
        {messages.map((msg, idx) => (
          <ChatMessage key={idx} message={msg.message}  type={msg.type} />
        ))}
        {postMessage.isPending && <ChatMessageLoading type={"received"} />}
      </div>
       
        

      <div className="flex flex-col items-start gap-2">
        <Textarea
          rows={2}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        >
        </Textarea>
          <Button onClick={handleSend}>Send</Button>
        
      </div>
    </div>
  )
}
export default App
