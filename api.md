# Shared Types

```python
from chunkify.types import ChunkifyError
```

# Assets

Types:

```python
from chunkify.types import Asset, AssetStatus
```

Methods:

- <code title="post /assets">client.assets.<a href="./src/chunkify/resources/assets/assets.py">create</a>(\*\*<a href="src/chunkify/types/asset_create_params.py">params</a>) -> <a href="./src/chunkify/types/asset.py">Asset</a></code>
- <code title="get /assets/{assetId}">client.assets.<a href="./src/chunkify/resources/assets/assets.py">retrieve</a>(asset_id) -> <a href="./src/chunkify/types/asset.py">Asset</a></code>
- <code title="patch /assets/{assetId}">client.assets.<a href="./src/chunkify/resources/assets/assets.py">update</a>(asset_id, \*\*<a href="src/chunkify/types/asset_update_params.py">params</a>) -> None</code>
- <code title="get /assets">client.assets.<a href="./src/chunkify/resources/assets/assets.py">list</a>(\*\*<a href="src/chunkify/types/asset_list_params.py">params</a>) -> <a href="./src/chunkify/types/asset.py">SyncPaginatedResults[Asset]</a></code>
- <code title="delete /assets/{assetId}">client.assets.<a href="./src/chunkify/resources/assets/assets.py">delete</a>(asset_id, \*\*<a href="src/chunkify/types/asset_delete_params.py">params</a>) -> None</code>

## Outputs

Types:

```python
from chunkify.types.assets import AssetOutput
```

Methods:

- <code title="post /assets/{assetId}/outputs">client.assets.outputs.<a href="./src/chunkify/resources/assets/outputs.py">create</a>(asset_id, \*\*<a href="src/chunkify/types/assets/output_create_params.py">params</a>) -> <a href="./src/chunkify/types/assets/asset_output.py">AssetOutput</a></code>
- <code title="get /assets/{assetId}/outputs/{outputId}">client.assets.outputs.<a href="./src/chunkify/resources/assets/outputs.py">retrieve</a>(output_id, \*, asset_id) -> <a href="./src/chunkify/types/assets/asset_output.py">AssetOutput</a></code>
- <code title="get /assets/{assetId}/outputs">client.assets.outputs.<a href="./src/chunkify/resources/assets/outputs.py">list</a>(asset_id, \*\*<a href="src/chunkify/types/assets/output_list_params.py">params</a>) -> <a href="./src/chunkify/types/assets/asset_output.py">SyncPaginatedResults[AssetOutput]</a></code>
- <code title="delete /assets/{assetId}/outputs/{outputId}">client.assets.outputs.<a href="./src/chunkify/resources/assets/outputs.py">delete</a>(output_id, \*, asset_id, \*\*<a href="src/chunkify/types/assets/output_delete_params.py">params</a>) -> None</code>

## Workflow

Types:

```python
from chunkify.types.assets import AssetActionRun
```

Methods:

- <code title="post /assets/{assetId}/workflow/update">client.assets.workflow.<a href="./src/chunkify/resources/assets/workflow.py">update</a>(asset_id) -> <a href="./src/chunkify/types/workflows/workflow_run.py">WorkflowRun</a></code>
- <code title="get /assets/{assetId}/workflow/actions">client.assets.workflow.<a href="./src/chunkify/resources/assets/workflow.py">list_actions</a>(asset_id, \*\*<a href="src/chunkify/types/assets/workflow_list_actions_params.py">params</a>) -> <a href="./src/chunkify/types/assets/asset_action_run.py">SyncPaginatedResults[AssetActionRun]</a></code>

# Events

Types:

```python
from chunkify.types import Event
```

Methods:

- <code title="get /events/{eventId}">client.events.<a href="./src/chunkify/resources/events.py">retrieve</a>(event_id) -> <a href="./src/chunkify/types/event.py">Event</a></code>
- <code title="get /events">client.events.<a href="./src/chunkify/resources/events.py">list</a>(\*\*<a href="src/chunkify/types/event_list_params.py">params</a>) -> <a href="./src/chunkify/types/event.py">SyncPaginatedResults[Event]</a></code>

# Files

Types:

```python
from chunkify.types import JobFile
```

Methods:

- <code title="get /files/{fileId}">client.files.<a href="./src/chunkify/resources/files.py">retrieve</a>(file_id) -> <a href="./src/chunkify/types/job_file.py">JobFile</a></code>
- <code title="get /files">client.files.<a href="./src/chunkify/resources/files.py">list</a>(\*\*<a href="src/chunkify/types/file_list_params.py">params</a>) -> <a href="./src/chunkify/types/job_file.py">SyncPaginatedResults[JobFile]</a></code>
- <code title="delete /files/{fileId}">client.files.<a href="./src/chunkify/resources/files.py">delete</a>(file_id) -> None</code>

# Jobs

Types:

```python
from chunkify.types import HlsAv1, HlsH264, HlsH265, Job, Jpg, MP4Av1, MP4H264, MP4H265, WebmVp9
```

Methods:

- <code title="post /jobs">client.jobs.<a href="./src/chunkify/resources/jobs/jobs.py">create</a>(\*\*<a href="src/chunkify/types/job_create_params.py">params</a>) -> <a href="./src/chunkify/types/job.py">Job</a></code>
- <code title="get /jobs/{jobId}">client.jobs.<a href="./src/chunkify/resources/jobs/jobs.py">retrieve</a>(job_id) -> <a href="./src/chunkify/types/job.py">Job</a></code>
- <code title="get /jobs">client.jobs.<a href="./src/chunkify/resources/jobs/jobs.py">list</a>(\*\*<a href="src/chunkify/types/job_list_params.py">params</a>) -> <a href="./src/chunkify/types/job.py">SyncPaginatedResults[Job]</a></code>
- <code title="delete /jobs/{jobId}">client.jobs.<a href="./src/chunkify/resources/jobs/jobs.py">delete</a>(job_id) -> None</code>
- <code title="post /jobs/{jobId}/cancel">client.jobs.<a href="./src/chunkify/resources/jobs/jobs.py">cancel</a>(job_id) -> None</code>

## Files

Types:

```python
from chunkify.types.jobs import FileListResponse
```

Methods:

- <code title="get /jobs/{jobId}/files">client.jobs.files.<a href="./src/chunkify/resources/jobs/files.py">list</a>(job_id) -> <a href="./src/chunkify/types/jobs/file_list_response.py">FileListResponse</a></code>

## Logs

Types:

```python
from chunkify.types.jobs import LogListResponse
```

Methods:

- <code title="get /jobs/{jobId}/logs">client.jobs.logs.<a href="./src/chunkify/resources/jobs/logs.py">list</a>(job_id, \*\*<a href="src/chunkify/types/jobs/log_list_params.py">params</a>) -> <a href="./src/chunkify/types/jobs/log_list_response.py">LogListResponse</a></code>

## Transcoders

Types:

```python
from chunkify.types.jobs import TranscoderListResponse
```

Methods:

- <code title="get /jobs/{jobId}/transcoders">client.jobs.transcoders.<a href="./src/chunkify/resources/jobs/transcoders.py">list</a>(job_id) -> <a href="./src/chunkify/types/jobs/transcoder_list_response.py">TranscoderListResponse</a></code>

# Metrics

Types:

```python
from chunkify.types import MetricsAssets, MetricsStorage, MetricsUsage
```

Methods:

- <code title="get /metrics/assets">client.metrics.<a href="./src/chunkify/resources/metrics.py">assets</a>(\*\*<a href="src/chunkify/types/metric_assets_params.py">params</a>) -> <a href="./src/chunkify/types/metrics_assets.py">MetricsAssets</a></code>
- <code title="get /metrics/storage">client.metrics.<a href="./src/chunkify/resources/metrics.py">storage</a>(\*\*<a href="src/chunkify/types/metric_storage_params.py">params</a>) -> <a href="./src/chunkify/types/metrics_storage.py">MetricsStorage</a></code>
- <code title="get /metrics/usage">client.metrics.<a href="./src/chunkify/resources/metrics.py">usage</a>(\*\*<a href="src/chunkify/types/metric_usage_params.py">params</a>) -> <a href="./src/chunkify/types/metrics_usage.py">MetricsUsage</a></code>

# Notifications

Types:

```python
from chunkify.types import Notification
```

Methods:

- <code title="post /notifications">client.notifications.<a href="./src/chunkify/resources/notifications.py">create</a>(\*\*<a href="src/chunkify/types/notification_create_params.py">params</a>) -> <a href="./src/chunkify/types/notification.py">Notification</a></code>
- <code title="get /notifications/{notificationId}">client.notifications.<a href="./src/chunkify/resources/notifications.py">retrieve</a>(notification_id) -> <a href="./src/chunkify/types/notification.py">Notification</a></code>
- <code title="get /notifications">client.notifications.<a href="./src/chunkify/resources/notifications.py">list</a>(\*\*<a href="src/chunkify/types/notification_list_params.py">params</a>) -> <a href="./src/chunkify/types/notification.py">SyncPaginatedResults[Notification]</a></code>
- <code title="delete /notifications/{notificationId}">client.notifications.<a href="./src/chunkify/resources/notifications.py">delete</a>(notification_id) -> None</code>

# Projects

Types:

```python
from chunkify.types import Project, ProjectListResponse
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/chunkify/resources/projects/projects.py">create</a>(\*\*<a href="src/chunkify/types/project_create_params.py">params</a>) -> <a href="./src/chunkify/types/project.py">Project</a></code>
- <code title="get /projects/{projectId}">client.projects.<a href="./src/chunkify/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/chunkify/types/project.py">Project</a></code>
- <code title="patch /projects/{projectId}">client.projects.<a href="./src/chunkify/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/chunkify/types/project_update_params.py">params</a>) -> None</code>
- <code title="get /projects">client.projects.<a href="./src/chunkify/resources/projects/projects.py">list</a>() -> <a href="./src/chunkify/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /projects/{projectId}">client.projects.<a href="./src/chunkify/resources/projects/projects.py">delete</a>(project_id) -> None</code>

## AnalyticsConnections

Types:

```python
from chunkify.types.projects import (
    AnalyticsConnection,
    AnalyticsConnectionCreateResponse,
    AnalyticsConnectionListResponse,
)
```

Methods:

- <code title="post /projects/{projectId}/analytics/connections">client.projects.analytics_connections.<a href="./src/chunkify/resources/projects/analytics_connections/analytics_connections.py">create</a>(project_id, \*\*<a href="src/chunkify/types/projects/analytics_connection_create_params.py">params</a>) -> <a href="./src/chunkify/types/projects/analytics_connection_create_response.py">AnalyticsConnectionCreateResponse</a></code>
- <code title="get /projects/{projectId}/analytics/connections/{connectionId}">client.projects.analytics_connections.<a href="./src/chunkify/resources/projects/analytics_connections/analytics_connections.py">retrieve</a>(connection_id, \*, project_id) -> <a href="./src/chunkify/types/projects/analytics_connection.py">AnalyticsConnection</a></code>
- <code title="patch /projects/{projectId}/analytics/connections/{connectionId}">client.projects.analytics_connections.<a href="./src/chunkify/resources/projects/analytics_connections/analytics_connections.py">update</a>(connection_id, \*, project_id, \*\*<a href="src/chunkify/types/projects/analytics_connection_update_params.py">params</a>) -> <a href="./src/chunkify/types/projects/analytics_connection.py">AnalyticsConnection</a></code>
- <code title="get /projects/{projectId}/analytics/connections">client.projects.analytics_connections.<a href="./src/chunkify/resources/projects/analytics_connections/analytics_connections.py">list</a>(project_id) -> <a href="./src/chunkify/types/projects/analytics_connection_list_response.py">AnalyticsConnectionListResponse</a></code>
- <code title="delete /projects/{projectId}/analytics/connections/{connectionId}">client.projects.analytics_connections.<a href="./src/chunkify/resources/projects/analytics_connections/analytics_connections.py">delete</a>(connection_id, \*, project_id) -> None</code>

### Keys

Types:

```python
from chunkify.types.projects.analytics_connections import (
    AnalyticsKey,
    KeyCreateResponse,
    KeyListResponse,
    KeyRotateResponse,
)
```

Methods:

- <code title="post /projects/{projectId}/analytics/connections/{connectionId}/keys">client.projects.analytics_connections.keys.<a href="./src/chunkify/resources/projects/analytics_connections/keys.py">create</a>(connection_id, \*, project_id, \*\*<a href="src/chunkify/types/projects/analytics_connections/key_create_params.py">params</a>) -> <a href="./src/chunkify/types/projects/analytics_connections/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /projects/{projectId}/analytics/connections/{connectionId}/keys">client.projects.analytics_connections.keys.<a href="./src/chunkify/resources/projects/analytics_connections/keys.py">list</a>(connection_id, \*, project_id) -> <a href="./src/chunkify/types/projects/analytics_connections/key_list_response.py">KeyListResponse</a></code>
- <code title="post /projects/{projectId}/analytics/connections/{connectionId}/keys/{keyId}/rotate">client.projects.analytics_connections.keys.<a href="./src/chunkify/resources/projects/analytics_connections/keys.py">rotate</a>(key_id, \*, project_id, connection_id) -> <a href="./src/chunkify/types/projects/analytics_connections/key_rotate_response.py">KeyRotateResponse</a></code>

# Sources

Types:

```python
from chunkify.types import Source
```

Methods:

- <code title="post /sources">client.sources.<a href="./src/chunkify/resources/sources.py">create</a>(\*\*<a href="src/chunkify/types/source_create_params.py">params</a>) -> <a href="./src/chunkify/types/source.py">Source</a></code>
- <code title="get /sources/{sourceId}">client.sources.<a href="./src/chunkify/resources/sources.py">retrieve</a>(source_id) -> <a href="./src/chunkify/types/source.py">Source</a></code>
- <code title="get /sources">client.sources.<a href="./src/chunkify/resources/sources.py">list</a>(\*\*<a href="src/chunkify/types/source_list_params.py">params</a>) -> <a href="./src/chunkify/types/source.py">SyncPaginatedResults[Source]</a></code>
- <code title="delete /sources/{sourceId}">client.sources.<a href="./src/chunkify/resources/sources.py">delete</a>(source_id) -> None</code>

# Storages

Types:

```python
from chunkify.types import Storage, StorageListResponse
```

Methods:

- <code title="post /storages">client.storages.<a href="./src/chunkify/resources/storages.py">create</a>(\*\*<a href="src/chunkify/types/storage_create_params.py">params</a>) -> <a href="./src/chunkify/types/storage.py">Storage</a></code>
- <code title="get /storages/{storageId}">client.storages.<a href="./src/chunkify/resources/storages.py">retrieve</a>(storage_id) -> <a href="./src/chunkify/types/storage.py">Storage</a></code>
- <code title="patch /storages/{storageId}">client.storages.<a href="./src/chunkify/resources/storages.py">update</a>(storage_id, \*\*<a href="src/chunkify/types/storage_update_params.py">params</a>) -> None</code>
- <code title="get /storages">client.storages.<a href="./src/chunkify/resources/storages.py">list</a>() -> <a href="./src/chunkify/types/storage_list_response.py">StorageListResponse</a></code>
- <code title="delete /storages/{storageId}">client.storages.<a href="./src/chunkify/resources/storages.py">delete</a>(storage_id) -> None</code>

# Thumbnails

Types:

```python
from chunkify.types import Thumbnail
```

Methods:

- <code title="post /thumbnails">client.thumbnails.<a href="./src/chunkify/resources/thumbnails.py">create</a>(\*\*<a href="src/chunkify/types/thumbnail_create_params.py">params</a>) -> <a href="./src/chunkify/types/thumbnail.py">Thumbnail</a></code>
- <code title="get /thumbnails/{thumbnailId}">client.thumbnails.<a href="./src/chunkify/resources/thumbnails.py">retrieve</a>(thumbnail_id) -> <a href="./src/chunkify/types/thumbnail.py">Thumbnail</a></code>
- <code title="get /thumbnails">client.thumbnails.<a href="./src/chunkify/resources/thumbnails.py">list</a>(\*\*<a href="src/chunkify/types/thumbnail_list_params.py">params</a>) -> <a href="./src/chunkify/types/thumbnail.py">SyncPaginatedResults[Thumbnail]</a></code>
- <code title="delete /thumbnails/{thumbnailId}">client.thumbnails.<a href="./src/chunkify/resources/thumbnails.py">delete</a>(thumbnail_id, \*\*<a href="src/chunkify/types/thumbnail_delete_params.py">params</a>) -> None</code>

# Tokens

Types:

```python
from chunkify.types import Token, TokenListResponse
```

Methods:

- <code title="post /tokens">client.tokens.<a href="./src/chunkify/resources/tokens.py">create</a>(\*\*<a href="src/chunkify/types/token_create_params.py">params</a>) -> <a href="./src/chunkify/types/token.py">Token</a></code>
- <code title="get /tokens">client.tokens.<a href="./src/chunkify/resources/tokens.py">list</a>() -> <a href="./src/chunkify/types/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /tokens/{tokenId}">client.tokens.<a href="./src/chunkify/resources/tokens.py">revoke</a>(token_id) -> None</code>

# Transcodings

Types:

```python
from chunkify.types import Transcoding
```

Methods:

- <code title="post /transcodings">client.transcodings.<a href="./src/chunkify/resources/transcodings.py">create</a>(\*\*<a href="src/chunkify/types/transcoding_create_params.py">params</a>) -> <a href="./src/chunkify/types/transcoding.py">Transcoding</a></code>
- <code title="get /transcodings/{transcodingId}">client.transcodings.<a href="./src/chunkify/resources/transcodings.py">retrieve</a>(transcoding_id) -> <a href="./src/chunkify/types/transcoding.py">Transcoding</a></code>
- <code title="get /transcodings">client.transcodings.<a href="./src/chunkify/resources/transcodings.py">list</a>(\*\*<a href="src/chunkify/types/transcoding_list_params.py">params</a>) -> <a href="./src/chunkify/types/transcoding.py">SyncPaginatedResults[Transcoding]</a></code>
- <code title="delete /transcodings/{transcodingId}">client.transcodings.<a href="./src/chunkify/resources/transcodings.py">delete</a>(transcoding_id, \*\*<a href="src/chunkify/types/transcoding_delete_params.py">params</a>) -> None</code>
- <code title="post /transcodings/{transcodingId}/cancel">client.transcodings.<a href="./src/chunkify/resources/transcodings.py">cancel</a>(transcoding_id) -> None</code>

# Uploads

Types:

```python
from chunkify.types import Upload
```

Methods:

- <code title="post /uploads">client.uploads.<a href="./src/chunkify/resources/uploads.py">create</a>(\*\*<a href="src/chunkify/types/upload_create_params.py">params</a>) -> <a href="./src/chunkify/types/upload.py">Upload</a></code>
- <code title="get /uploads/{uploadId}">client.uploads.<a href="./src/chunkify/resources/uploads.py">retrieve</a>(upload_id) -> <a href="./src/chunkify/types/upload.py">Upload</a></code>
- <code title="get /uploads">client.uploads.<a href="./src/chunkify/resources/uploads.py">list</a>(\*\*<a href="src/chunkify/types/upload_list_params.py">params</a>) -> <a href="./src/chunkify/types/upload.py">SyncPaginatedResults[Upload]</a></code>
- <code title="delete /uploads/{uploadId}">client.uploads.<a href="./src/chunkify/resources/uploads.py">delete</a>(upload_id) -> None</code>
- <code title="post /uploads/completion/{token}">client.uploads.<a href="./src/chunkify/resources/uploads.py">complete</a>(token, \*\*<a href="src/chunkify/types/upload_complete_params.py">params</a>) -> None</code>

# Webhooks

Types:

```python
from chunkify.types import Webhook, WebhookListResponse, NewEventWebhookEvent, UnwrapWebhookEvent
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/chunkify/resources/webhooks.py">create</a>(\*\*<a href="src/chunkify/types/webhook_create_params.py">params</a>) -> <a href="./src/chunkify/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks/{webhookId}">client.webhooks.<a href="./src/chunkify/resources/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/chunkify/types/webhook.py">Webhook</a></code>
- <code title="patch /webhooks/{webhookId}">client.webhooks.<a href="./src/chunkify/resources/webhooks.py">update</a>(webhook_id, \*\*<a href="src/chunkify/types/webhook_update_params.py">params</a>) -> None</code>
- <code title="get /webhooks">client.webhooks.<a href="./src/chunkify/resources/webhooks.py">list</a>() -> <a href="./src/chunkify/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhookId}">client.webhooks.<a href="./src/chunkify/resources/webhooks.py">delete</a>(webhook_id) -> None</code>

# Workflows

Types:

```python
from chunkify.types import Workflow
```

Methods:

- <code title="post /workflows">client.workflows.<a href="./src/chunkify/resources/workflows/workflows.py">create</a>(\*\*<a href="src/chunkify/types/workflow_create_params.py">params</a>) -> <a href="./src/chunkify/types/workflow.py">Workflow</a></code>
- <code title="get /workflows/{workflowId}">client.workflows.<a href="./src/chunkify/resources/workflows/workflows.py">retrieve</a>(workflow_id) -> <a href="./src/chunkify/types/workflow.py">Workflow</a></code>
- <code title="patch /workflows/{workflowId}">client.workflows.<a href="./src/chunkify/resources/workflows/workflows.py">update</a>(workflow_id, \*\*<a href="src/chunkify/types/workflow_update_params.py">params</a>) -> None</code>
- <code title="get /workflows">client.workflows.<a href="./src/chunkify/resources/workflows/workflows.py">list</a>(\*\*<a href="src/chunkify/types/workflow_list_params.py">params</a>) -> <a href="./src/chunkify/types/workflow.py">SyncPaginatedResults[Workflow]</a></code>
- <code title="delete /workflows/{workflowId}">client.workflows.<a href="./src/chunkify/resources/workflows/workflows.py">delete</a>(workflow_id) -> None</code>

## Revisions

Types:

```python
from chunkify.types.workflows import WorkflowRevision
```

Methods:

- <code title="get /workflows/{workflowId}/revisions/{revision}">client.workflows.revisions.<a href="./src/chunkify/resources/workflows/revisions.py">retrieve</a>(revision, \*, workflow_id) -> <a href="./src/chunkify/types/workflows/workflow_revision.py">WorkflowRevision</a></code>

## Runs

Types:

```python
from chunkify.types.workflows import WorkflowRun
```

Methods:

- <code title="get /workflows/{workflowId}/runs/{runId}">client.workflows.runs.<a href="./src/chunkify/resources/workflows/runs/runs.py">retrieve</a>(run_id, \*, workflow_id) -> <a href="./src/chunkify/types/workflows/workflow_run.py">WorkflowRun</a></code>
- <code title="get /workflows/{workflowId}/runs">client.workflows.runs.<a href="./src/chunkify/resources/workflows/runs/runs.py">list</a>(workflow_id, \*\*<a href="src/chunkify/types/workflows/run_list_params.py">params</a>) -> <a href="./src/chunkify/types/workflows/workflow_run.py">SyncPaginatedResults[WorkflowRun]</a></code>

### Actions

Methods:

- <code title="get /workflows/{workflowId}/runs/{runId}/actions/{actionRunId}">client.workflows.runs.actions.<a href="./src/chunkify/resources/workflows/runs/actions.py">retrieve</a>(action_run_id, \*, workflow_id, run_id) -> <a href="./src/chunkify/types/assets/asset_action_run.py">AssetActionRun</a></code>
- <code title="get /workflows/{workflowId}/runs/{runId}/actions">client.workflows.runs.actions.<a href="./src/chunkify/resources/workflows/runs/actions.py">list</a>(run_id, \*, workflow_id, \*\*<a href="src/chunkify/types/workflows/runs/action_list_params.py">params</a>) -> <a href="./src/chunkify/types/assets/asset_action_run.py">SyncPaginatedResults[AssetActionRun]</a></code>
