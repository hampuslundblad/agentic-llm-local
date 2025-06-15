type ChatMessageType =   "sent" | "received"

export type ChatMessageProps =  {
  type: ChatMessageType
}

const ChatMessageLoading = ({  type, }: ChatMessageProps) => {
  return (
    <div className={`flex ${getChatMessageAlignmentClass(type)}`}  >
      <div className={`inline-block bg-blue-500 text-gray-900 px-6 py-4 rounded-2xl max-w-xs relative`}>
        <div className="flex items-center space-x-2">
          <TypingIndicator />
        </div>
      </div>
    </div>
  )
}

const TypingIndicator = () => (
  <div className="flex space-x-1">
    <span className="block w-2 h-2 bg-gray-500 rounded-full animate-bounce [animation-delay:-0.32s]"></span>
    <span className="block w-2 h-2 bg-gray-500 rounded-full animate-bounce [animation-delay:-0.16s]"></span>
    <span className="block w-2 h-2 bg-gray-500 rounded-full animate-bounce"></span>
  </div>
)

const getChatMessageAlignmentClass = (type: ChatMessageType) => {
    switch (type) {
        case "sent":
        return "justify-end";
        case "received":
        return "justify-start";
        default:
        return "justify-start";
    }
    }

export default ChatMessageLoading
