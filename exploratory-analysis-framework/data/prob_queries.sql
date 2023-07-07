SELECT merge_scenarios.id as ms_id, merge_scenarios.project_id as pr_id, merge_scenarios.has_conflict as has_conflict, merge_scenarios.commit_merge as commit_merge_id, merge_commit_hash as mc_hash, files.filepath as filepath, files.has_conflict as f_has_conflict FROM merge_scenarios INNER JOIN files ON files.merge_scenarios_id=merge_scenarios.id;

['ms_id', 'pr_id', 'has_conflict', 'commit_merge_id', 'mc_hash', 'filepath', 'f_has_conflict']

SELECT merge_scenarios.id as ms_id, merge_scenarios.project_id as pr_id, merge_scenarios.has_conflict as has_conflict, merge_scenarios.commit_merge as commit_merge_id, merge_commit_hash as mc_hash, files.filepath as filepath, files.has_conflict as f_has_conflict, chunks.begin_line, chunks.end_line, chunks.has_conflict as c_has_conflict FROM merge_scenarios INNER JOIN files ON files.merge_scenarios_id=merge_scenarios.id INNER JOIN chunks ON chunks.file_id=files.id;

['ms_id', 'pr_id', 'has_conflict', 'commit_merge_id', 'mc_hash', 'filepath', 'f_has_conflict', 'begin_line', 'end_line', 'c_has_conflict']
