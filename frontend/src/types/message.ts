export interface Message {
  id: number;
  customer_name: string;
  email: string;
  text: string;
  status: string;
  created_at: string;
  updated_at: string;
  reviewed_at: string | null;
}

export interface Analysis {
  id: number;
  message_id: number;
  summary: string;
  category: string;
  priority: string;
  confidence: number;
  suggested_reply: string;
  created_at: string;
  updated_at: string;
}