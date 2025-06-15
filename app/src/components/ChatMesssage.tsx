type ChatMessageType = "sent" | "received"

export type ChatMessageProps = {
  type: ChatMessageType
  message: string
}

const ChatMessage = ({ message, type }: ChatMessageProps) => {
  return (
    <div className={`flex ${getChatMessageAlignmentClass(type)}`}>
      <div
        className={`inline-block ${getBackgroundColor(type)} ${getTextColor(type)} px-4 py-2 rounded-2xl max-w-xs relative`}
      >
        {message}
        {/* <span c
        lassName="absolute left-6 -bottom-2 w-0 h-0 border-t-8 border-t-gray-200 border-l-8 border-l-transparent border-r-8 border-r-transparent"></span> */}
      </div>
    </div>
  )
}

const getTextColor = (type: ChatMessageType) => {
  switch (type) {
    case "sent":
      return "text-blue-900"
    case "received":
      return "text-white"
    default:
      return "text-gray-900"
  }
}

const getBackgroundColor = (type: ChatMessageType) => {
  switch (type) {
    case "sent":
      return "bg-gray-200 text-blue-900"
    case "received":
      return "bg-blue-500 text-gray-900"
    default:
      return "bg-gray-200 text-gray-900"
  }
}

const getChatMessageAlignmentClass = (type: ChatMessageType) => {
  switch (type) {
    case "sent":
      return "justify-end"
    case "received":
      return "justify-start"
    default:
      return "justify-start"
  }
}

export default ChatMessage
