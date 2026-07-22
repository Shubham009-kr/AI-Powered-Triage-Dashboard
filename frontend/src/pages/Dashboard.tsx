import MessageDetails from "../components/MessageDetails";
import MessageList from "../components/MessageList";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="mx-auto max-w-7xl">

        <header className="mb-6">
          <h1 className="text-3xl font-bold text-slate-900">
            AI Support Triage Dashboard
          </h1>

          <p className="mt-2 text-slate-600">
            Analyze and prioritize customer support messages using AI.
          </p>
        </header>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">

          <section className="rounded-xl bg-white p-5 shadow">
            <h2 className="mb-4 text-lg font-semibold">
              Messages
            </h2>

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