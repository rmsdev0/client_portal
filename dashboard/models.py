# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AgentActivity(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    activity_id = models.CharField(max_length=16)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255, blank=True)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    activity = models.CharField(max_length=13)
    duration = models.BigIntegerField()
    detail = models.CharField(max_length=255, blank=True)
    pending_time = models.BigIntegerField(blank=True, null=True)
    talk_time = models.BigIntegerField(blank=True, null=True)
    hold_time = models.BigIntegerField(blank=True, null=True)
    acw_time = models.BigIntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True)
    origination_number = models.CharField(max_length=255, blank=True)
    destination_number = models.CharField(max_length=255, blank=True)
    external_number = models.CharField(max_length=255, blank=True)
    other_party_phone_type = models.CharField(max_length=8, blank=True)
    disposition = models.CharField(max_length=19, blank=True)
    agent_disposition_name = models.CharField(max_length=255, blank=True)
    agent_disposition_code = models.IntegerField(blank=True, null=True)
    agent_disposition_notes = models.TextField(blank=True)
    session_id = models.CharField(max_length=16, blank=True)
    media_type = models.CharField(max_length=8, blank=True)
    case_number = models.CharField(max_length=48, blank=True)

    class Meta:
        managed = False
        db_table = 'agent_activity'


class AgentDispositions(models.Model):
    disposition_name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_dispositions'


class AgentPerformance(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255, blank=True)
    no_service = models.TextField()  # This field type is a guess.
    service_name = models.CharField(max_length=255)
    is_internal = models.TextField()  # This field type is a guess.
    is_campaign = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    total_num_calls = models.BigIntegerField()
    num_calls_in = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_out = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    num_calls_agent_abandoned = models.BigIntegerField(blank=True, null=True)
    num_calls_rejected = models.BigIntegerField()
    num_calls_no_answer = models.BigIntegerField()
    num_calls_graded = models.BigIntegerField()
    num_initiated_transfers = models.BigIntegerField()
    total_login_time = models.BigIntegerField()
    total_working_time = models.BigIntegerField()
    total_ready_time = models.BigIntegerField()
    total_handling_time = models.BigIntegerField()
    total_handling_call_time = models.BigIntegerField()
    total_handling_call_time_in = models.BigIntegerField()
    total_handling_call_time_out = models.BigIntegerField()
    total_handling_acw_time = models.BigIntegerField()
    total_handling_acw_time_in = models.BigIntegerField()
    total_handling_acw_time_out = models.BigIntegerField()
    total_busy_time_in = models.BigIntegerField()
    total_busy_time_out = models.BigIntegerField()
    total_ringing_time_in = models.BigIntegerField()
    total_ringing_time_out = models.BigIntegerField()
    total_acw_time_in = models.BigIntegerField()
    total_acw_time_out = models.BigIntegerField()
    total_hold_time_in = models.BigIntegerField()
    total_hold_time_out = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    grade_name = models.CharField(max_length=255, blank=True)
    grade_count = models.BigIntegerField()
    grade_total_value = models.BigIntegerField()
    grade_order_num = models.IntegerField(blank=True, null=True)
    not_ready_reason = models.CharField(max_length=255, blank=True)
    not_ready_time = models.BigIntegerField(blank=True, null=True)
    num_emails_pulled = models.BigIntegerField()
    num_emails_received_as_transfers = models.BigIntegerField()
    num_emails_replied_by_agent = models.BigIntegerField()
    num_emails_closed_without_reply = models.BigIntegerField()
    num_emails_discarded = models.BigIntegerField()
    email_answer_time = models.BigIntegerField()
    num_emails_in_carried_over = models.BigIntegerField()
    num_emails_in_waiting_in_personal_queues = models.BigIntegerField()
    num_emails_in_waiting_in_personal_queues_breached_sla = models.BigIntegerField()
    num_emails_out_waiting_in_personal_queues = models.BigIntegerField()
    num_emails_in_service_changed = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'agent_performance'


class AgentSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agent_state_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=7)
    proficiency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_skills'


class AgentStates(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255)
    media_type = models.CharField(max_length=8, blank=True)
    direction = models.CharField(max_length=8, blank=True)
    service_name = models.CharField(max_length=255, blank=True)
    workitem_id = models.CharField(max_length=255, blank=True)
    rank = models.CharField(max_length=255, blank=True)
    agent_capacity = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=15)
    is_connected = models.TextField(blank=True)  # This field type is a guess.
    was_connected = models.TextField(blank=True)  # This field type is a guess.
    not_ready_reason = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    session_id = models.CharField(max_length=16, blank=True)
    screen_recorder_id = models.CharField(max_length=16, blank=True)
    screen_recording_url = models.CharField(max_length=255, blank=True)
    encryption_key_id = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'agent_states'


class Agents(models.Model):
    login_id = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255, blank=True)
    rank = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agents'


class AggregatorRuns(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    period_start_time = models.DateTimeField()
    period_end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    num_records_aggregated = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=13, blank=True)

    class Meta:
        managed = False
        db_table = 'aggregator_runs'


class CallDetail(models.Model):
    id = models.CharField(unique=True, max_length=16, blank=True)
    pkid = models.IntegerField(primary_key=True)
    agg_run_id = models.CharField(max_length=16)
    media_type = models.CharField(max_length=8, blank=True)
    start_time = models.DateTimeField()
    ivr_time = models.BigIntegerField()
    queue_time = models.BigIntegerField()
    pending_time = models.BigIntegerField()
    talk_time = models.BigIntegerField()
    hold_time = models.BigIntegerField()
    acw_time = models.BigIntegerField()
    duration = models.BigIntegerField()
    service_name = models.CharField(max_length=255, blank=True)
    scenario_name = models.CharField(max_length=255, blank=True)
    trunk_description = models.CharField(max_length=255, blank=True)
    caller_login_id = models.CharField(max_length=255, blank=True)
    callee_login_id = models.CharField(max_length=255, blank=True)
    caller_phone_type = models.CharField(max_length=8, blank=True)
    callee_phone_type = models.CharField(max_length=8, blank=True)
    caller_rank = models.CharField(max_length=255, blank=True)
    callee_rank = models.CharField(max_length=255, blank=True)
    from_phone = models.CharField(max_length=255, blank=True)
    original_destination_phone = models.CharField(max_length=255, blank=True)
    connected_to_phone = models.CharField(max_length=255, blank=True)
    transferred_from_phone = models.CharField(max_length=255, blank=True)
    disposition = models.CharField(max_length=20, blank=True)
    agent_disposition_name = models.CharField(max_length=255, blank=True)
    agent_disposition_code = models.IntegerField(blank=True, null=True)
    agent_disposition_notes = models.TextField(blank=True)
    reported_problem = models.CharField(max_length=18, blank=True)
    initial_call_id = models.CharField(max_length=16, blank=True)
    initial_start_time = models.DateTimeField(blank=True, null=True)
    initial_service_name = models.CharField(max_length=255, blank=True)
    initial_caller_phone_type = models.CharField(max_length=8, blank=True)
    initial_callee_phone_type = models.CharField(max_length=8, blank=True)
    initial_from_phone = models.CharField(max_length=255, blank=True)
    initial_original_destination_phone = models.CharField(max_length=255, blank=True)
    initial_connected_to_phone = models.CharField(max_length=255, blank=True)
    flagged = models.TextField(blank=True)  # This field type is a guess.
    voice_signature = models.TextField(blank=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True)
    caller_first_name = models.CharField(max_length=255, blank=True)
    callee_first_name = models.CharField(max_length=255, blank=True)
    caller_last_name = models.CharField(max_length=255, blank=True)
    callee_last_name = models.CharField(max_length=255, blank=True)
    email_id = models.CharField(max_length=48, blank=True)
    email_subject = models.CharField(max_length=1024, blank=True)
    case_id = models.CharField(max_length=48, blank=True)
    thread_id = models.CharField(max_length=48, blank=True)
    case_number = models.CharField(max_length=48, blank=True)
    case_search_result = models.CharField(max_length=48, blank=True)
    response_email_id = models.CharField(max_length=48, blank=True)
    caller_monitored = models.TextField(blank=True)  # This field type is a guess.
    callee_monitored = models.TextField(blank=True)  # This field type is a guess.
    caller_interaction_step_id = models.CharField(max_length=16, blank=True)
    callee_interaction_step_id = models.CharField(max_length=16, blank=True)
    caller_rtp_server_id = models.CharField(max_length=16, blank=True)
    caller_recording_url = models.CharField(max_length=255, blank=True)
    caller_cpa_rtp_server_id = models.CharField(max_length=16, blank=True)
    caller_cpa_recording_url = models.CharField(max_length=255, blank=True)
    caller_encryption_key_id = models.CharField(max_length=16, blank=True)
    callee_rtp_server_id = models.CharField(max_length=16, blank=True)
    callee_recording_url = models.CharField(max_length=255, blank=True)
    callee_cpa_rtp_server_id = models.CharField(max_length=16, blank=True)
    callee_cpa_recording_url = models.CharField(max_length=255, blank=True)
    callee_encryption_key_id = models.CharField(max_length=16, blank=True)
    email_detail_id = models.CharField(unique=True, max_length=48, blank=True)
    email_kb_article_id = models.CharField(max_length=48, blank=True)
    caller_team_name = models.CharField(max_length=255, blank=True)
    callee_team_name = models.CharField(max_length=255, blank=True)
    detail_record_count = models.IntegerField(blank=True, null=True)
    caller_has_screen_recording = models.CharField(max_length=16, blank=True)
    callee_has_screen_recording = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'call_detail'


class CallbackCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True)
    num_calls_queued = models.BigIntegerField(blank=True, null=True)
    num_callbacks_requested = models.BigIntegerField(blank=True, null=True)
    num_callbacks_attempted = models.BigIntegerField(blank=True, null=True)
    num_callbacks_busy = models.BigIntegerField(blank=True, null=True)
    num_callbacks_no_answer = models.BigIntegerField(blank=True, null=True)
    num_callbacks_answered = models.BigIntegerField(blank=True, null=True)
    num_callbacks_requeued = models.BigIntegerField(blank=True, null=True)
    num_callbacks_abandoned = models.BigIntegerField(blank=True, null=True)
    num_callbacks_handled = models.BigIntegerField(blank=True, null=True)
    callback_wait_time = models.BigIntegerField(blank=True, null=True)
    callback_customer_answer_time = models.BigIntegerField(blank=True, null=True)
    callback_agent_answer_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callback_counters'


class ConcurrentUsers(models.Model):
    pkid = models.IntegerField(primary_key=True)
    num_users = models.IntegerField(blank=True, null=True)
    users = models.TextField(blank=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    agg_run_id = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'concurrent_users'


class Databasechangelog(models.Model):
    id = models.CharField(db_column='ID', max_length=63, primary_key=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=63)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=200)  # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED')  # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED')  # Field name made lowercase.
    exectype = models.CharField(db_column='EXECTYPE', max_length=10)  # Field name made lowercase.
    md5sum = models.CharField(db_column='MD5SUM', max_length=35, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=255, blank=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True)  # Field name made lowercase.
    liquibase = models.CharField(db_column='LIQUIBASE', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangelog'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED')  # Field name made lowercase.
    lockgranted = models.DateTimeField(db_column='LOCKGRANTED', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LOCKEDBY', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class DeferredAggregatedInteractions(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'deferred_aggregated_interactions'


class DeferredInteractionStepSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=7)
    service_level = models.IntegerField(blank=True, null=True)
    service_level_threshold = models.IntegerField(blank=True, null=True)
    short_abandonment_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deferred_interaction_step_skills'


class DeferredInteractionSteps(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    prev_interaction_step_id = models.CharField(max_length=16, blank=True)
    next_interaction_step_id = models.CharField(max_length=16, blank=True)
    interaction_id = models.CharField(max_length=16)
    scenario_id = models.CharField(max_length=16)
    scenario_name = models.CharField(max_length=255)
    direction = models.CharField(max_length=8)
    login_id = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255, blank=True)
    rank = models.CharField(max_length=255, blank=True)
    agent_capacity = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ivr_start_time = models.DateTimeField(blank=True, null=True)
    ivr_end_time = models.DateTimeField(blank=True, null=True)
    queue_start_time = models.DateTimeField(blank=True, null=True)
    queue_end_time = models.DateTimeField(blank=True, null=True)
    pending_start_time = models.DateTimeField(blank=True, null=True)
    pending_end_time = models.DateTimeField(blank=True, null=True)
    delivered_start_time = models.DateTimeField(blank=True, null=True)
    delivered_end_time = models.DateTimeField(blank=True, null=True)
    delivered_duration = models.BigIntegerField(blank=True, null=True)
    hold_duration = models.BigIntegerField(blank=True, null=True)
    wrap_up_start_time = models.DateTimeField(blank=True, null=True)
    wrap_up_end_time = models.DateTimeField(blank=True, null=True)
    wrap_up_duration = models.BigIntegerField(blank=True, null=True)
    total_duration = models.BigIntegerField(blank=True, null=True)
    route_result = models.CharField(max_length=19, blank=True)
    priority = models.IntegerField()
    overflow = models.TextField()  # This field type is a guess.
    monitored = models.TextField()  # This field type is a guess.
    direct = models.TextField()  # This field type is a guess.
    result = models.CharField(max_length=21, blank=True)
    rtp_server_id = models.CharField(max_length=16, blank=True)
    recording_url = models.CharField(max_length=255, blank=True)
    cpa_rtp_server_id = models.CharField(max_length=16, blank=True)
    cpa_recording_url = models.CharField(max_length=255, blank=True)
    encryption_key_id = models.CharField(max_length=16, blank=True)
    workitem_id = models.CharField(max_length=255, blank=True)
    service_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    phone_type = models.CharField(max_length=15, blank=True)
    external_number = models.CharField(max_length=255, blank=True)
    bridge_interaction_step_id = models.CharField(max_length=16, blank=True)
    linked_interaction_step_id = models.CharField(max_length=16, blank=True)
    qm_mode = models.CharField(max_length=11, blank=True)
    monitored_interaction_step_id = models.CharField(max_length=16, blank=True)
    trunk_description = models.CharField(max_length=255, blank=True)
    disposition_name = models.CharField(max_length=255, blank=True)
    disposition_code = models.IntegerField(blank=True, null=True)
    disposition_notes = models.TextField(blank=True)
    voice_signature = models.TextField(blank=True)  # This field type is a guess.
    self_service = models.TextField(blank=True)  # This field type is a guess.
    reported_problem = models.CharField(max_length=18, blank=True)
    screen_recorder_id = models.CharField(max_length=16, blank=True)
    screen_recording_url = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'deferred_interaction_steps'


class DeferredInteractions(models.Model):
    record_id = models.CharField(primary_key=True, max_length=16)
    id = models.CharField(max_length=16, blank=True)
    waiting_for_initiator_id = models.CharField(max_length=16, blank=True)
    waiting_for_initiated_by_id = models.CharField(max_length=16, blank=True)
    waiting_for_initiated_by_reason = models.CharField(max_length=28, blank=True)
    scenario_context_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    media_type = models.CharField(max_length=8)
    duration = models.BigIntegerField(blank=True, null=True)
    origination = models.CharField(max_length=255, blank=True)
    destination = models.CharField(max_length=255, blank=True)
    initiated_by_interaction_id = models.CharField(max_length=16, blank=True)
    flagged = models.TextField(blank=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True)
    direction = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'deferred_interactions'


class DeferredSurveys(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)
    created_time = models.DateTimeField()
    fcr = models.TextField(blank=True)  # This field type is a guess.
    nps = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deferred_surveys'


class DispositionCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True)
    disposition_name = models.CharField(max_length=255, blank=True)
    disposition_code = models.CharField(max_length=255, blank=True)
    is_campaign = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True)
    num_records_completed = models.BigIntegerField()
    num_calls_received = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_preview_items = models.BigIntegerField()
    num_campaign_calls = models.BigIntegerField()
    num_non_campaign_calls_inbound = models.BigIntegerField()
    num_non_campaign_calls_outbound = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'disposition_counters'


class ExternalChatTranscripts(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    interaction_id = models.CharField(max_length=16)
    session_id = models.CharField(max_length=16, blank=True)
    content = models.TextField(blank=True)
    encryption_key_id = models.CharField(max_length=16, blank=True)
    encrypted_content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'external_chat_transcripts'


class InteractionQualityMonitoring(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16, blank=True)
    response_email_id = models.CharField(max_length=48, blank=True)
    review_time = models.DateTimeField()
    review_agent_login_id = models.CharField(max_length=255)
    review_agent_first_name = models.CharField(max_length=255)
    review_agent_last_name = models.CharField(max_length=255)
    review_notes = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'interaction_quality_monitoring'


class InteractionQualityMonitoringGrades(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    iqm_id = models.CharField(max_length=16)
    grade_name = models.CharField(max_length=255, blank=True)
    grade_value = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_quality_monitoring_grades'


class InteractionStepSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=7)
    service_level = models.IntegerField(blank=True, null=True)
    service_level_threshold = models.IntegerField(blank=True, null=True)
    short_abandonment_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_step_skills'


class InteractionSteps(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    prev_interaction_step_id = models.CharField(max_length=16, blank=True)
    next_interaction_step_id = models.CharField(max_length=16, blank=True)
    interaction_id = models.CharField(max_length=16)
    scenario_id = models.CharField(max_length=16)
    scenario_name = models.CharField(max_length=255)
    direction = models.CharField(max_length=8)
    login_id = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255, blank=True)
    rank = models.CharField(max_length=255, blank=True)
    agent_capacity = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ivr_start_time = models.DateTimeField(blank=True, null=True)
    ivr_end_time = models.DateTimeField(blank=True, null=True)
    queue_start_time = models.DateTimeField(blank=True, null=True)
    queue_end_time = models.DateTimeField(blank=True, null=True)
    pending_start_time = models.DateTimeField(blank=True, null=True)
    pending_end_time = models.DateTimeField(blank=True, null=True)
    delivered_start_time = models.DateTimeField(blank=True, null=True)
    delivered_end_time = models.DateTimeField(blank=True, null=True)
    delivered_duration = models.BigIntegerField(blank=True, null=True)
    hold_duration = models.BigIntegerField(blank=True, null=True)
    wrap_up_start_time = models.DateTimeField(blank=True, null=True)
    wrap_up_end_time = models.DateTimeField(blank=True, null=True)
    wrap_up_duration = models.BigIntegerField(blank=True, null=True)
    total_duration = models.BigIntegerField(blank=True, null=True)
    route_result = models.CharField(max_length=19, blank=True)
    priority = models.IntegerField()
    overflow = models.TextField()  # This field type is a guess.
    monitored = models.TextField()  # This field type is a guess.
    direct = models.TextField()  # This field type is a guess.
    result = models.CharField(max_length=21, blank=True)
    rtp_server_id = models.CharField(max_length=16, blank=True)
    recording_url = models.CharField(max_length=255, blank=True)
    cpa_rtp_server_id = models.CharField(max_length=16, blank=True)
    cpa_recording_url = models.CharField(max_length=255, blank=True)
    encryption_key_id = models.CharField(max_length=16, blank=True)
    workitem_id = models.CharField(max_length=255, blank=True)
    service_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    phone_type = models.CharField(max_length=15, blank=True)
    external_number = models.CharField(max_length=255, blank=True)
    bridge_interaction_step_id = models.CharField(max_length=16, blank=True)
    linked_interaction_step_id = models.CharField(max_length=16, blank=True)
    qm_mode = models.CharField(max_length=11, blank=True)
    monitored_interaction_step_id = models.CharField(max_length=16, blank=True)
    trunk_description = models.CharField(max_length=255, blank=True)
    disposition_name = models.CharField(max_length=255, blank=True)
    disposition_code = models.IntegerField(blank=True, null=True)
    disposition_notes = models.TextField(blank=True)
    voice_signature = models.TextField(blank=True)  # This field type is a guess.
    self_service = models.TextField(blank=True)  # This field type is a guess.
    reported_problem = models.CharField(max_length=18, blank=True)
    screen_recorder_id = models.CharField(max_length=16, blank=True)
    screen_recording_url = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'interaction_steps'


class Interactions(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    scenario_context_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    media_type = models.CharField(max_length=8)
    duration = models.BigIntegerField(blank=True, null=True)
    origination = models.CharField(max_length=255, blank=True)
    destination = models.CharField(max_length=255, blank=True)
    initiated_by_interaction_id = models.CharField(max_length=16, blank=True)
    flagged = models.TextField(blank=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True)
    direction = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'interactions'


class OverflowCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True)
    destination_phone = models.CharField(max_length=255, blank=True)
    routed_to = models.CharField(max_length=255)
    is_overflow = models.TextField()  # This field type is a guess.
    no_team = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True)
    num_calls_received = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    handling_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'overflow_counters'


class Ranks(models.Model):
    rank = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ranks'


class RequestedSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    media_type = models.CharField(max_length=8, blank=True)
    skill_name = models.CharField(max_length=255)
    skill_group_name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=7)
    total_answer_time = models.BigIntegerField()
    num_calls_received = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_overflow = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'requested_skills'


class ScenarioContexts(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    interaction_end_time = models.DateTimeField()
    steps = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'scenario_contexts'


class ScenarioStepsCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    scenario_name = models.CharField(max_length=255, blank=True)
    block_type = models.CharField(max_length=50)
    block_title = models.CharField(max_length=255)
    exit_id = models.CharField(max_length=50)
    caller_disconnect = models.TextField()  # This field type is a guess.
    num_steps = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'scenario_steps_counters'


class Scenarios(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scenarios'


class ServiceInTimeCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True)
    destination_phone = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255, blank=True)
    media_type = models.CharField(max_length=8, blank=True)
    num_calls_received = models.BigIntegerField()
    num_calls_received_as_transfers = models.BigIntegerField()
    num_calls_received_as_transfers_from_same_service = models.BigIntegerField()
    num_calls_received_as_transfers_from_other_service = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_transferred_internally = models.BigIntegerField()
    num_calls_transferred_externally = models.BigIntegerField()
    answer_time = models.BigIntegerField()
    num_calls_abandoned = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    num_calls_abandoned_in_ivr = models.BigIntegerField()
    num_calls_self_service = models.BigIntegerField()
    num_calls_in_service_level = models.BigIntegerField()
    num_overflow_calls = models.BigIntegerField()
    num_calls_held = models.BigIntegerField()
    num_calls_recv_as_transfers_answered = models.BigIntegerField()
    num_calls_recv_as_transfers_in_service_level = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_in_ivr = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_after_threshold = models.BigIntegerField()
    num_calls_recv_as_transfers_queued = models.BigIntegerField()
    num_calls_recv_as_transfers_held = models.BigIntegerField()
    num_calls_queued_answered = models.BigIntegerField()
    answer_time_queued = models.BigIntegerField()
    num_calls_queued_abandoned = models.BigIntegerField()
    num_calls_queued_abandoned_after_threshold = models.BigIntegerField()
    num_calls_queued_in_service_level = models.BigIntegerField()
    num_calls_queued_held = models.BigIntegerField()
    abandonment_time_queued = models.BigIntegerField()
    abandonment_time_after_threshold_queued = models.BigIntegerField()
    abandonment_time = models.BigIntegerField()
    abandonment_time_after_threshold = models.BigIntegerField()
    total_duration_in = models.BigIntegerField()
    busy_time_in = models.BigIntegerField()
    busy_time_out = models.BigIntegerField()
    acw_time = models.BigIntegerField()
    acw_time_in = models.BigIntegerField()
    acw_time_out = models.BigIntegerField()
    hold_time_in = models.BigIntegerField()
    hold_time_out = models.BigIntegerField()
    ringing_time_in = models.BigIntegerField()
    ringing_time_out = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    num_calls_held_outbound = models.BigIntegerField()
    ready_time = models.BigIntegerField()
    not_ready_time = models.BigIntegerField()
    login_time = models.BigIntegerField()
    handling_time = models.BigIntegerField()
    handling_call_time = models.BigIntegerField()
    handling_acw_time = models.BigIntegerField()
    assigned_handling_call_time = models.BigIntegerField()
    assigned_handling_acw_time = models.BigIntegerField()
    min_agents = models.BigIntegerField(blank=True, null=True)
    max_agents = models.BigIntegerField(blank=True, null=True)
    campaign_calls_attempted = models.BigIntegerField()
    campaign_dialer_calls_queued = models.BigIntegerField()
    campaign_dialer_calls_handled = models.BigIntegerField()
    campaign_calls_ivr = models.BigIntegerField()
    campaign_calls_queued = models.BigIntegerField()
    campaign_calls_abandoned = models.BigIntegerField()
    campaign_calls_handled = models.BigIntegerField()
    campaign_calls_held = models.BigIntegerField()
    campaign_calls_rpc = models.BigIntegerField()
    campaign_calls_unattended = models.BigIntegerField()
    campaign_records_completed = models.BigIntegerField()
    campaign_records_valid = models.BigIntegerField()
    campaign_records_dialed = models.BigIntegerField()
    campaign_records_queued = models.BigIntegerField()
    campaign_records_handled = models.BigIntegerField()
    campaign_records_excluded = models.BigIntegerField()
    campaign_records_rpc = models.BigIntegerField()
    campaign_ivr_time = models.BigIntegerField()
    campaign_queue_time = models.BigIntegerField()
    campaign_abandonment_time = models.BigIntegerField()
    campaign_answer_time = models.BigIntegerField()
    campaign_talk_time = models.BigIntegerField()
    campaign_hold_time = models.BigIntegerField()
    campaign_acw_time = models.BigIntegerField()
    campaign_handling_call_time = models.BigIntegerField()
    campaign_handling_acw_time = models.BigIntegerField()
    campaign_assigned_handling_call_time = models.BigIntegerField()
    campaign_assigned_handling_acw_time = models.BigIntegerField()
    campaign_preview_items = models.BigIntegerField()
    campaign_preview_time = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    num_emails_replied_by_agent = models.BigIntegerField()
    num_emails_closed_without_reply = models.BigIntegerField()
    email_routing_time = models.BigIntegerField()
    email_reply_time = models.BigIntegerField()
    num_emails_carried_over = models.BigIntegerField()
    num_emails_in_progress = models.BigIntegerField()
    num_emails_remaining_in_personal_queues = models.BigIntegerField()
    num_emails_remaining_in_personal_queues_breached_sla = models.BigIntegerField()
    num_emails_in_service_changed = models.BigIntegerField()
    num_emails_in_service_changed_received = models.BigIntegerField()
    num_emails_received_new = models.BigIntegerField()
    num_emails_carried_over_new = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_in_time_counters'


class ServicePerformance(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True)
    destination_phone = models.CharField(max_length=255, blank=True)
    media_type = models.CharField(max_length=8, blank=True)
    num_calls_received = models.BigIntegerField()
    num_calls_received_as_transfers = models.BigIntegerField()
    num_calls_received_as_transfers_from_same_service = models.BigIntegerField()
    num_calls_received_as_transfers_from_other_service = models.BigIntegerField()
    num_calls_transferred_internally = models.BigIntegerField()
    num_calls_transferred_externally = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    answer_time = models.BigIntegerField()
    num_calls_in_service_level = models.BigIntegerField()
    num_calls_abandoned = models.BigIntegerField()
    num_calls_abandoned_in_ivr = models.BigIntegerField()
    num_calls_abandoned_short = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    abandonment_time = models.BigIntegerField()
    abandonment_time_except_short = models.BigIntegerField()
    abandonment_time_after_threshold = models.BigIntegerField()
    num_calls_self_service = models.BigIntegerField()
    num_calls_overflow = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_held = models.BigIntegerField()
    handling_time_in = models.BigIntegerField()
    talk_time_in = models.BigIntegerField()
    hold_time_in = models.BigIntegerField()
    wrap_up_time_in = models.BigIntegerField()
    num_calls_recv_as_transfers_answered = models.BigIntegerField()
    num_calls_recv_as_transfers_in_service_level = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_in_ivr = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_short = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_after_threshold = models.BigIntegerField()
    num_calls_recv_as_transfers_queued = models.BigIntegerField()
    num_calls_recv_as_transfers_held = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    handling_time_out = models.BigIntegerField()
    talk_time_out = models.BigIntegerField()
    wrap_up_time_out = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    campaign_calls_attempted = models.BigIntegerField()
    campaign_dialer_calls_queued = models.BigIntegerField()
    campaign_dialer_calls_handled = models.BigIntegerField()
    campaign_calls_ivr = models.BigIntegerField()
    campaign_calls_queued = models.BigIntegerField()
    campaign_calls_abandoned = models.BigIntegerField()
    campaign_calls_handled = models.BigIntegerField()
    campaign_calls_held = models.BigIntegerField()
    campaign_calls_rpc = models.BigIntegerField()
    campaign_calls_unattended = models.BigIntegerField()
    campaign_records_completed = models.BigIntegerField()
    campaign_records_valid = models.BigIntegerField()
    campaign_records_dialed = models.BigIntegerField()
    campaign_records_queued = models.BigIntegerField()
    campaign_records_handled = models.BigIntegerField()
    campaign_records_excluded = models.BigIntegerField()
    campaign_records_rpc = models.BigIntegerField()
    campaign_ivr_time = models.BigIntegerField()
    campaign_queue_time = models.BigIntegerField()
    campaign_abandonment_time = models.BigIntegerField()
    campaign_answer_time = models.BigIntegerField()
    campaign_talk_time = models.BigIntegerField()
    campaign_hold_time = models.BigIntegerField()
    campaign_acw_time = models.BigIntegerField()
    campaign_handling_call_time = models.BigIntegerField()
    campaign_handling_acw_time = models.BigIntegerField()
    campaign_assigned_handling_call_time = models.BigIntegerField()
    campaign_assigned_handling_acw_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_performance'


class Skills(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=7)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'skills'


class Surveys(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)
    created_time = models.DateTimeField()
    fcr = models.TextField(blank=True)  # This field type is a guess.
    nps = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveys'


class TeamPerformance(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    team_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    total_num_calls = models.BigIntegerField()
    num_calls_in = models.BigIntegerField()
    num_calls_out = models.BigIntegerField()
    num_calls_agent_abandoned = models.BigIntegerField(blank=True, null=True)
    num_calls_rejected = models.BigIntegerField()
    num_initiated_transfers = models.BigIntegerField()
    total_login_time = models.BigIntegerField()
    total_working_time = models.BigIntegerField()
    total_ready_time = models.BigIntegerField()
    total_busy_time_in = models.BigIntegerField()
    total_busy_time_out = models.BigIntegerField()
    total_ringing_time = models.BigIntegerField()
    total_acw_time = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'team_performance'


class Teams(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'teams'


#**** end bright pattern models ****
class CrmInfo(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=120)
    user_name = models.CharField(max_length=50)
    pswd = models.CharField(max_length=50)


class CampaignList(models.Model):
    client_id = models.IntegerField()
    campaign_name = models.CharField(max_length=200)

    def __str__(self):
        return self.campaign_name

