# Railway Deployment Status

## Latest Deployment: October 16, 2025

### Issue Identified
- **Problem**: Railway health check returning 400 Bad Request
- **Error**: `"GET /api/ HTTP/1.1" 400 143 "-" "RailwayHealthCheck/1.0"`
- **Root Cause**: `ALLOWED_HOSTS` not including Railway's internal domains

### Fix Applied
**Commit**: `Fix: Add Railway domains to ALLOWED_HOSTS for health checks`

**Changes Made**:
```python
# Added to settings.py:
if not DEBUG:
    ALLOWED_HOSTS.append('.railway.app')
    ALLOWED_HOSTS.append('.up.railway.app')
```

This ensures that:
1. ✅ Railway health checks can reach the app
2. ✅ Internal Railway domains are accepted
3. ✅ Custom domains continue to work (via environment variable)

### Deployment Triggered
- **Method**: Git push to `develop` branch
- **Time**: Just now
- **Expected**: 2-5 minutes for build and deploy

### What to Monitor

#### 1. Health Check Status
The health check should now return `200 OK` instead of `400`:
```bash
# Watch for this in logs:
"GET /api/ HTTP/1.1" 200 ...  "RailwayHealthCheck/1.0"
```

#### 2. Check Deployment in Railway UI
- Go to Railway dashboard
- Select **development** environment
- Check **Deployments** tab
- Look for latest commit: "Fix: Add Railway domains to ALLOWED_HOSTS for health checks"

#### 3. Test Endpoints
Once deployed, test:

```bash
# Health check (should work now)
curl https://crm-dev.davethedev.co.nz/api/

# Test API endpoint
curl https://crm-dev.davethedev.co.nz/api/companies/

# Test custom domain
curl https://crm-dev.davethedev.co.nz/
```

### Known Outstanding Issues

#### CSRF 403 Errors (Still Present)
Users still getting 403 errors on login/register forms:
```
POST /register/ HTTP/1.1" 403
POST /login/ HTTP/1.1" 403
```

**Why**: The `CSRF_TRUSTED_ORIGINS` needs to include the custom domain.

**Solution**: Already set via Railway environment variable, but may need to verify:
```bash
railway variables --kv | grep CSRF_TRUSTED_ORIGINS
```

Should include: `https://crm-dev.davethedev.co.nz`

### Next Steps

1. **Wait for deployment** (2-5 minutes)
2. **Check logs** for successful health check
3. **Test custom domain** in browser
4. **If CSRF still fails**, verify environment variables are correct:
   ```bash
   railway variables --kv
   ```
5. **Test login/register** to confirm CSRF is resolved

### Environment Variables to Verify

Both **development** and **production** should have:

```bash
ALLOWED_HOSTS=crm-dev.davethedev.co.nz,django-crm-api-development.up.railway.app
CSRF_TRUSTED_ORIGINS=https://crm-dev.davethedev.co.nz,https://django-crm-api-development.up.railway.app
DEBUG=False
```

(Adjust for production environment accordingly)

### Timeline

- ✅ **20:46 UTC**: Identified health check 400 error
- ✅ **20:47 UTC**: Applied fix to settings.py
- ✅ **20:48 UTC**: Committed and pushed to develop
- ⏳ **20:48-20:53 UTC**: Deployment in progress
- ⏳ **After deploy**: Test and verify

---

## How to Check Logs

```bash
# Real-time logs
railway logs --tail 50

# Or check Railway UI:
# Dashboard > Select Service > Deployments > Latest > View Logs
```

## Quick Test Commands

```bash
# Test health endpoint
curl -I https://crm-dev.davethedev.co.nz/api/

# Test main page
curl -I https://crm-dev.davethedev.co.nz/

# Check DNS
dig crm-dev.davethedev.co.nz +short
```

---

**Status**: 🔄 Deployment in progress...
