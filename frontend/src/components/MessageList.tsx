import { useEffect } from "react";

import { useMessageStore } from "../store/messageStore";
import LoadingSpinner from "./LoadingSpinner";

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
    return <LoadingSpinner />;
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
          <div className="flex items-start justify-between">
            <div>
                <p className="font-semibold">
                    {message.customer_name}
                </p>

                <p className="text-sm text-slate-500">
                    {message.email}
                </p>
            </div>

            <span className="rounded-full bg-slate-100 px-2 py-1 text-xs font-medium uppercase">
                {message.status}
            </span>
          </div>
        </button>
      ))}
    </div>
  );
}