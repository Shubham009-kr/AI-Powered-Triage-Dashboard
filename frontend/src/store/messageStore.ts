import { create } from "zustand";

import api from "../api/api";
import type { Analysis, Message } from "../types/message";


interface MessageStore {
  messages: Message[];
  selectedMessage: Message | null;
  analysis: Analysis | null;

  loading: boolean;
  analysisLoading: boolean;

  fetchMessages: () => Promise<void>;
  analyzeMessage: (messageId: number) => Promise<void>;

  selectMessage: (message: Message) => void;
}

export const useMessageStore = create<MessageStore>((set) => ({
  messages: [],
  selectedMessage: null,
  analysis: null,

  loading: false,
  analysisLoading: false,

  fetchMessages: async () => {
    set({ loading: true });

    try {
        const response = await api.get<Message[]>("/messages");

        set({
        messages: response.data,
        });
    } catch (error) {
        console.error("Failed to fetch messages:", error);
    } finally {
        set({
        loading: false,
        });
    } 
  },

  analyzeMessage: async (messageId) => {
    set({
        analysisLoading: true,
        analysis: null,
    });

  try {
    const response = await api.post<Analysis>(
      `/messages/${messageId}/analyze`
    );

    set({
      analysis: response.data,
    });
  } catch (error) {
    console.error("Failed to analyze message:", error);
  } finally {
        set({
        analysisLoading: false,
        });
    }
  },

  selectMessage: (message) =>
    set({
      selectedMessage: message,
      analysis: null,
    }),
}));