import { useMessageStore } from "../store/messageStore";
import LoadingSpinner from "./LoadingSpinner";

export default function AnalysisPanel() {
  const { analysis, analysisLoading } = useMessageStore();

  if (analysisLoading) {
    return <LoadingSpinner />;
  }

  if (!analysis) {
    return (
      <div className="rounded-lg border border-dashed p-8 text-center text-slate-500">
        Click <strong>Analyze Message</strong> to generate an AI summary.
      </div>
    );
  }

  return (
    <div className="space-y-5 rounded-lg border bg-slate-50 p-5">
      <div>
        <h3 className="font-semibold">Summary</h3>
        <p className="mt-1">{analysis.summary}</p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <h3 className="font-semibold">Category</h3>
          <p>{analysis.category}</p>
        </div>

        <div>
          <h3 className="font-semibold">Priority</h3>
            <span
                className={`rounded-full px-3 py-1 text-sm font-medium
                ${
                    analysis.priority === "high"
                        ? "bg-red-100 text-red-700"
                        : analysis.priority === "medium"
                        ? "bg-yellow-100 text-yellow-700"
                        : "bg-green-100 text-green-700"
                }`}
            >
                {analysis.priority.charAt(0).toUpperCase() +
                    analysis.priority.slice(1)}
            </span>
        </div>

        <div>
            <h3 className="font-semibold mb-2">
                Confidence
            </h3>

            <div className="h-3 overflow-hidden rounded-full bg-slate-200">
                <div
                    className="h-full bg-blue-600"
                    style={{
                        width: `${analysis.confidence * 100}%`,
                    }}
                />
            </div>

            <p className="mt-2 text-sm text-slate-600">
                {(analysis.confidence * 100).toFixed(0)}%
            </p>
        </div>
      </div>

      <div>
        <h3 className="font-semibold">Suggested Reply</h3>

        <div className="mt-2 rounded-md bg-white p-3 border">
          {analysis.suggested_reply}
        </div>
      </div>
    </div>
  );
}