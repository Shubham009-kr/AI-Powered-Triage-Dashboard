import MessageDetails from "../components/MessageDetails";
import MessageList from "../components/MessageList";
import { useMessageStore } from "../store/messageStore";

export default function Dashboard() {
  const { messages } = useMessageStore();

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(148,163,184,0.15),_transparent_35%),linear-gradient(to_right,rgba(148,163,184,0.14)_1px,transparent_1px),linear-gradient(to_bottom,rgba(148,163,184,0.14)_1px,transparent_1px)] bg-[size:100%_100%,32px_32px,32px_32px] p-6 text-slate-800">
      <div className="mx-auto max-w-7xl">

        <header className="mb-8 border-b border-slate-300 pb-5">
          <h1 className="text-3xl font-bold text-slate-900">
            AI Support Triage Dashboard
          </h1>

          <p className="mt-2 text-slate-600">
            Analyze and prioritize customer support messages using AI.
          </p>
        </header>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">

          <section className="rounded-xl bg-white p-5 shadow">
            <div className="mb-5 flex items-center justify-between">
                <h2 className="text-lg font-semibold">
                    Messages
                </h2>

                <span className="rounded-full bg-slate-100 px-3 py-1 text-sm">
                    {messages.length}
                </span>
            </div>

            <MessageList />
          </section>

          <section className="rounded-xl bg-white p-5 shadow lg:col-span-2">
            <h2 className="mb-4 text-lg font-semibold">
              Message Details
            </h2>

            <MessageDetails />
          </section>

        </div>

      </div>
    </div>
  );
}