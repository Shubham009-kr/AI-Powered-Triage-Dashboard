import { useMessageStore } from "../store/messageStore";
import AnalysisPanel from "./AnalysisPanel";

export default function MessageDetails() {
  const { selectedMessage, analyzeMessage, analysisLoading, } = useMessageStore();

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

        <div className="mb-4 flex items-center justify-between">
            <button
                onClick={() => analyzeMessage(selectedMessage.id)}
                disabled={analysisLoading}
                className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-slate-400"
            >
                {analysisLoading ? "Analyzing..." : "Analyze Message"}
            </button>
        </div>

        <AnalysisPanel />

        <div className="rounded-lg border mt-4 bg-slate-50 p-4 leading-relaxed">
          {selectedMessage.text}
        </div>
      </div>
    </div>
  );
}