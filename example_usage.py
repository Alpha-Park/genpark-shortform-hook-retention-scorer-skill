from client import ShortformHookRetentionScorerClient

def main():
    client = ShortformHookRetentionScorerClient()
    res = client.score_video_hook()
    print('Hook Retention Scorer: ' + res['hook_audit_id'] + ' (Score: ' + str(res['hook_viral_score']) + '/100)')
    print('Curiosity Gap: ' + res['curiosity_gap_grade'] + ' | Est. Retention: ' + str(res['estimated_3sec_retention_pct']) + '%')
    print('Dossier URL: ' + res['hook_dossier_url'])

if __name__ == '__main__':
    main()
