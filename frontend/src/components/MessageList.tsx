import { useEffect, useState } from "react";

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

  const [currentPage, setCurrentPage] = useState(1);

  const messagesPerPage = 5;

  useEffect(() => {
    fetchMessages();
  }, [fetchMessages]);

  if (loading) {
    return <LoadingSpinner />;
  }

  const totalPages = Math.ceil(messages.length / messagesPerPage);

  const startIndex = (currentPage - 1) * messagesPerPage;
  const currentMessages = messages.slice(
    startIndex,
    startIndex + messagesPerPage
  );

  return (
    <div className="space-y-3">
      {currentMessages.map((message) => (
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

      <div className="flex items-center justify-between border-t pt-4">
        <button
          onClick={() => setCurrentPage((page) => page - 1)}
          disabled={currentPage === 1}
          className="rounded-md bg-slate-200 px-3 py-2 text-sm font-medium hover:bg-slate-300 disabled:cursor-not-allowed disabled:opacity-50"
        >
          Previous
        </button>

        <span className="text-sm text-slate-600">
          Page {currentPage} of {totalPages}
        </span>

        <button
          onClick={() => setCurrentPage((page) => page + 1)}
          disabled={currentPage === totalPages}
          className="rounded-md bg-slate-200 px-3 py-2 text-sm font-medium hover:bg-slate-300 disabled:cursor-not-allowed disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
  );
}