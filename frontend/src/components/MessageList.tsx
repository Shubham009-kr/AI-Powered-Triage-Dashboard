import { useEffect } from "react";

import { useMessageStore } from "../store/messageStore";

export default function MessageList() {
  const {
    messages,
    loading,
    fetchMessages,
    selectMessage,
    selectedMessage,
  } = useMessageStore();

  useEffect(() => {
    fetchMessages();
  }, [fetchMessages]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="space-y-3">
      {messages.map((message) => (
        <button
          key={message.id}
          onClick={() => selectMessage(message)}
          className={`w-full rounded-lg border p-3 text-left transition-colors ${
            selectedMessage?.id === message.id
              ? "border-blue-500 bg-blue-50"
              : "border-slate-200 hover:bg-slate-50"
          }`}
        >
          <p className="font-medium">
            {message.customer_name}
          </p>

          <p className="text-sm text-slate-500">
            {message.email}
          </p>
        </button>
      ))}
    </div>
  );
}