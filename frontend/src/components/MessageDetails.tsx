import { useMessageStore } from "../store/messageStore";

export default function MessageDetails() {
  const { selectedMessage } = useMessageStore();

  if (!selectedMessage) {
    return (
      <div className="flex h-full items-center justify-center text-slate-400">
        Select a message to view details.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-semibold">
          {selectedMessage.customer_name}
        </h2>

        <p className="text-slate-600">
          {selectedMessage.email}
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div>
          <p className="text-sm font-medium text-slate-500">
            Status
          </p>

          <p className="mt-1 rounded-md bg-slate-100 px-3 py-2">
            {selectedMessage.status}
          </p>
        </div>

        <div>
          <p className="text-sm font-medium text-slate-500">
            Created At
          </p>

          <p className="mt-1 rounded-md bg-slate-100 px-3 py-2">
            {new Date(selectedMessage.created_at).toLocaleString()}
          </p>
        </div>
      </div>

      <div>
        <h3 className="mb-2 text-lg font-semibold">
          Original Message
        </h3>

        <div className="rounded-lg border bg-slate-50 p-4 leading-relaxed">
          {selectedMessage.text}
        </div>
      </div>
    </div>
  );
}