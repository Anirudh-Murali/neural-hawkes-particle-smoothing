class LogProbRecorder(object):
    def __init__(self, all_log_proposals, all_num_unobs):
        self.all_log_proposals = all_log_proposals
        self.all_num_unobs = all_num_unobs
        total_log_proposal, total_num_unobs = 0.0, 0.0
        all_avg_proposals = []
        for log_proposal, num_unobs in zip(self.all_log_proposals, self.all_num_unobs):
            total_log_proposal += log_proposal
            total_num_unobs += num_unobs
            if num_unobs > 0.5:
                all_avg_proposals.append(log_proposal / num_unobs)
        self.all_avg_proposals = np.array(all_avg_proposals, dtype=np.float32)
        self.avg_proposal = total_log_proposal / total_num_unobs