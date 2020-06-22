# File: `MatcherGenericTypeExtractor.java`

## Method: `public static Class genericTypeOfMatcher(Class matcherClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class genericTypeOfMatcher(Class matcherClass)", "entityFile": "MatcherGenericTypeExtractor.java"} -->Gets the generic type of given matcher. For example,
        for matcher class that extends BaseMatcher[Integer] this method returns Integer

# File: `InvocationOnMock.java`

## Method: `T getArgumentAt(int index, Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "T getArgumentAt(int index, Class<T> clazz)", "entityFile": "InvocationOnMock.java"} -->Returns casted argument using position
        @param index argument position
        @param clazz argument type
        @return casted argument on position

## Method: `Object callRealMethod() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "Object callRealMethod() throws Throwable", "entityFile": "InvocationOnMock.java"} -->calls real method
        Warning: depending on the real implementation it might throw exceptions
        @return whatever the real method returns / throws
        @throws Throwable in case real method throws

# File: `ReturnsDeepStubs.java`

## Method: `private Object newDeepStubMock(GenericMetadataSupport returnTypeGenericMetadata, Object parentMock)`

        <!-- META {"entityType": "Method", "entitySignature": "private Object newDeepStubMock(GenericMetadataSupport returnTypeGenericMetadata, Object parentMock)", "entityFile": "ReturnsDeepStubs.java"} -->Creates a mock using the Generics Metadata.
        Finally as we want to mock the actual type, but we want to pass along the contextual generics meta-data
        that was resolved for the current return type, for this to happen we associate to the mock an new instance of
        ReturnsDeepStubs answer in which we will store the returned type generic metadata.
        @param returnTypeGenericMetadata The metadata to use to create the new mock.
        @param parentMock The parent of the current deep stub mock.
        @return The mock

# File: `InvocationOnMock.java`

## Interface: `InvocationOnMock`

        <!-- META {"entityType": "Interface", "entitySignature": "InvocationOnMock", "entityFile": "InvocationOnMock.java"} -->An invocation on a mock
        A placeholder for mock, the method that was called and the arguments that were passed.

# File: `InvocationNotifierHandler.java`

## Class: `InvocationNotifierHandler`

        <!-- META {"entityType": "Class", "entitySignature": "InvocationNotifierHandler", "entityFile": "InvocationNotifierHandler.java"} -->Handler, that call all listeners wanted for this mock, before delegating it
        to the parameterized handler.
        Also imposterize MockHandlerImpl, delegate all call of InternalMockHandler to the real mockHandler

# File: `MockHandler.java`

## Method: `Object handle(Invocation invocation) throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "Object handle(Invocation invocation) throws Throwable", "entityFile": "MockHandler.java"} -->Takes an invocation object and handles it.
        The default implementation provided by Mockito handles invocations by recording
        method calls on mocks for further verification, captures the stubbing information when mock is stubbed,
        returns the stubbed values for invocations that have been stubbed, and much more.
        @param invocation The invocation to handle
        @return Result
        @throws Throwable Throwable

## Interface: `MockHandler`

        <!-- META {"entityType": "Interface", "entitySignature": "MockHandler", "entityFile": "MockHandler.java"} -->Mockito handler of an invocation on a mock. This is a core part of the API, the heart of Mockito.
        See also the org.mockito.plugins.MockMaker.
        This api is work in progress. Do not provide your own implementations.
        Mockito will provide you with the implementation via other org.mockito.plugins.MockMaker methods.

# File: `ReturnsDeepStubs.java`

## Class: `ReturnsDeepStubs`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsDeepStubs", "entityFile": "ReturnsDeepStubs.java"} -->Returning deep stub implementation.
        Will return previously created mock if the invocation matches.
        Supports nested generic information, with this answer you can write code like this :
        <pre class="code"><code class="java">
        interface GenericsNest&lt;K extends Comparable&lt;K&gt; & Cloneable&gt; extends Map&lt;K, Set&lt;Number&gt;&gt; {}
        GenericsNest&lt;?&gt; mock = mock(GenericsNest.class, new ReturnsGenericDeepStubs());
        Number number = mock.entrySet().iterator().next().getValue().iterator().next();
        @see org.mockito.Mockito#RETURNS_DEEP_STUBS
        @see org.mockito.Answers#RETURNS_DEEP_STUBS

# File: `StubInfo.java`

## Interface: `StubInfo`

        <!-- META {"entityType": "Interface", "entitySignature": "StubInfo", "entityFile": "StubInfo.java"} -->The information about stubbing, for example the location of stubbing.

# File: `MockitoJUnit.java`

## Method: `public static MockitoRule rule()`

        <!-- META {"entityType": "Method", "entitySignature": "public static MockitoRule rule()", "entityFile": "MockitoJUnit.java"} -->Creates rule instance that initiates @Mocks
        See MockitoRule.
        @return the rule instance

# File: `MockHandlerImpl.java`

## Class: `MockHandlerImpl`

        <!-- META {"entityType": "Class", "entitySignature": "MockHandlerImpl", "entityFile": "MockHandlerImpl.java"} -->Invocation handler set on mock objects.
        @param <T> type of mock object to handle

# File: `MockitoJUnit.java`

## Method: `public static VerificationCollector collector()`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationCollector collector()", "entityFile": "MockitoJUnit.java"} -->Creates a rule instance that can perform lazy verifications.
        @see VerificationCollector
        @return the rule instance

## Class: `MockitoJUnit`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoJUnit", "entityFile": "MockitoJUnit.java"} -->The JUnit rule can be used instead of org.mockito.runners.MockitoJUnitRunner. See MockitoRule.
        @since 1.10.17

# File: `NullResultGuardian.java`

## Class: `NullResultGuardian`

        <!-- META {"entityType": "Class", "entitySignature": "NullResultGuardian", "entityFile": "NullResultGuardian.java"} -->Protects the results from delegate MockHandler. Makes sure the results are valid.
        by Szczepan Faber, created at: 5/22/12

# File: `Description.java`

## Method: `public Description(VerificationMode verification, String description)`

        <!-- META {"entityType": "Method", "entitySignature": "public Description(VerificationMode verification, String description)", "entityFile": "Description.java"} -->Constructs a verification mode which wraps the given verification mode.
        @param verification The implementation to use for verification
        @param description The failure message to prepend if verification fails

## Method: `public void verify(VerificationData data)`

        <!-- META {"entityType": "Method", "entitySignature": "public void verify(VerificationData data)", "entityFile": "Description.java"} -->Performs verification using the wrapped verification mode implementation.
        Prepends the custom failure message if verification fails.
        @param data

# File: `InOrderImpl.java`

## Class: `InOrderImpl`

        <!-- META {"entityType": "Class", "entitySignature": "InOrderImpl", "entityFile": "InOrderImpl.java"} -->Allows verifying in order. This class should not be exposed, hence default access.

# File: `Description.java`

## Class: `Description`

        <!-- META {"entityType": "Class", "entitySignature": "Description", "entityFile": "Description.java"} -->Description verification mode wraps an existing verification mode and prepends
        a custom message to the assertion error if verification fails.
        @author Geoff.Schoeman
        @since 2.0.0

# File: `ReturnsEmptyValues.java`

## Class: `ReturnsEmptyValues`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsEmptyValues", "entityFile": "ReturnsEmptyValues.java"} -->Default answer of every Mockito mock.
        Returns appropriate primitive for primitive-returning methods
        Returns consistent values for primitive wrapper classes (e.g. int-returning method returns 0 and Integer-returning method returns 0, too)
        Returns empty collection for collection-returning methods (works for most commonly used collection types)
        Returns description of mock for toString() method
        Returns zero if references are equals otherwise non-zero for Comparable#compareTo(T other) method (see issue 184)
        Returns null for everything else

# File: `MockitoJUnitRule.java`

## Method: `public MockitoJUnitRule()`

        <!-- META {"entityType": "Method", "entitySignature": "public MockitoJUnitRule()", "entityFile": "MockitoJUnitRule.java"} -->Please use MockitoJUnit#rule().
        The reason of the deprecation is that we want to avoid concrete classes in the public api.

## Method: `public MockitoJUnitRule(Object targetTest)`

        <!-- META {"entityType": "Method", "entitySignature": "public MockitoJUnitRule(Object targetTest)", "entityFile": "MockitoJUnitRule.java"} -->Please use MockitoJUnit#rule().
        The reason of the deprecation is that we want to avoid concrete classes in the public api.

## Class: `MockitoJUnitRule`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoJUnitRule", "entityFile": "MockitoJUnitRule.java"} -->Please use MockitoJUnit#rule() instead of direct use.
        The reason of the deprecation is that we want to avoid concrete classes in the public api.
        @see MockitoJUnit
        @since 1.10.6

# File: `MockitoRule.java`

## Interface: `MockitoRule`

        <!-- META {"entityType": "Interface", "entitySignature": "MockitoRule", "entityFile": "MockitoRule.java"} -->The JUnit rule can be used instead of org.mockito.runners.MockitoJUnitRunner.
        It requires JUnit at least 4.7.
        This rule adds following behavior:
        Initializes mocks annotated with org.mockito.Mock,
        so that explicit usage of org.mockito.MockitoAnnotations#initMocks(Object) is not necessary.
        Mocks are initialized before each test method.
        validates framework usage after each test method. See javadoc for org.mockito.Mockito#validateMockitoUsage().
        Example use:
        <pre class="code"><code class="java">
        public class ExampleTest {
        @Rule
        public MockitoRule rule = MockitoJUnit.rule();
        @Mock
        private List list;
        @Test
        public void shouldDoSomething() {
        list.add(100);
        }
        }
        @since 1.10.17

# File: `ReturnsMoreEmptyValues.java`

## Class: `ReturnsMoreEmptyValues`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsMoreEmptyValues", "entityFile": "ReturnsMoreEmptyValues.java"} -->It's likely this implementation will be used by default by every Mockito 2.0 mock.
        Currently used only by Mockito#RETURNS_SMART_NULLS
        Current version of Mockito mocks by deafult use ReturnsEmptyValues
        Returns appropriate primitive for primitive-returning methods
        Returns consistent values for primitive wrapper classes (e.g. int-returning method retuns 0 and Integer-returning method returns 0, too)
        Returns empty collection for collection-returning methods (works for most commonly used collection types)
        Returns empty array for array-returning methods
        Returns "" for String-returning method
        Returns description of mock for toString() method
        Returns non-zero for Comparable#compareTo(T other) method (see issue 184)
        Returns null for everything else

# File: `VerificationCollector.java`

## Method: `T verify(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "T verify(T mock)", "entityFile": "VerificationCollector.java"} -->Lazily verify certain behaviour happened once.
        @see org.mockito.Mockito#verify(Object)
        @param <T> The type of the mock
        @param mock to be verified
        @return mock object itself

## Method: `T verify(T mock, VerificationMode mode)`

        <!-- META {"entityType": "Method", "entitySignature": "T verify(T mock, VerificationMode mode)", "entityFile": "VerificationCollector.java"} -->Lazily verify certain behaviour happened at least once / exact number of times / never.
        @see org.mockito.Mockito#verify(Object, VerificationMode)
        @param mock to be verified
        @param mode times(x), atLeastOnce() or never()
        @param <T> The type of the mock
        @return mock object itself

## Method: `void collectAndReport() throws MockitoAssertionError`

        <!-- META {"entityType": "Method", "entitySignature": "void collectAndReport() throws MockitoAssertionError", "entityFile": "VerificationCollector.java"} -->Collect all lazily verified behaviour. If there were failed verifications, it will
        throw a MockitoAssertionError containing all messages indicating the failed verifications.
        @throws MockitoAssertionError If there were failed verifications

# File: `VerificationModeFactory.java`

## Method: `public static VerificationMode description(VerificationMode mode, String description)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode description(VerificationMode mode, String description)", "entityFile": "VerificationModeFactory.java"} -->Verification mode will prepend the specified failure message if verification fails with the given implementation.
        @param mode Implementation used for verification
        @param description The custom failure message
        @return VerificationMode
        @since 2.0.0

# File: `AllInvocationsFinder.java`

## Method: `public List<Invocation> find(List<?> mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Invocation> find(List<?> mocks)", "entityFile": "AllInvocationsFinder.java"} -->gets all invocations from mocks. Invocations are ordered earlier first.
        @param mocks mocks
        @return invocations

# File: `VerificationCollector.java`

## Interface: `VerificationCollector`

        <!-- META {"entityType": "Interface", "entitySignature": "VerificationCollector", "entityFile": "VerificationCollector.java"} -->Use this rule in order to collect multiple verification failures and report at once.
        In the example below, the verification failure thrown by byteReturningMethod() does not block
        verifying against the simpleMethod(). After the test is run, a report is generated stating all
        collect verification failures.
        <pre class="code"><code class="java">
        @Rule
        public VerificationCollector collector = MockitoJUnit.collector();
        @Test
        public void should_fail() {
        IMethods methods = mock(IMethods.class);
        collector.verify(methods).byteReturningMethod();
        collector.verify(methods).simpleMethod();
        }
        @see org.mockito.Mockito#verify(Object)
        @see org.mockito.Mockito#verify(Object, VerificationMode)

# File: `ReturnsSmartNulls.java`

## Class: `ReturnsSmartNulls`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsSmartNulls", "entityFile": "ReturnsSmartNulls.java"} --><!-- 36fc2376-a231-11e9-87a8-333445793454 <=< ACCEPT -->Optional Answer that can be used with
        Mockito#mock(Class, Answer)
        This implementation can be helpful when working with legacy code. Unstubbed
        methods often return null. If your code uses the object returned by an
        unstubbed call you get a NullPointerException. This implementation of
        Answer returns SmartNulls instead of nulls.
        SmartNull gives nicer exception message than NPE because it points out the
        line where unstubbed method was called. You just click on the stack trace.
        ReturnsSmartNulls first tries to return ordinary return values (see
        ReturnsMoreEmptyValues) then it tries to return SmartNull. If the
        return type is not mockable (e.g. final) then ordinary null is returned.
        ReturnsSmartNulls will be probably the default return values strategy in
        Mockito 2.0<!-- ACCEPT >=> 36fc2376-a231-11e9-87a8-333445793454 -->

# File: `VerificationOverTimeImpl.java`

## Method: `public VerificationOverTimeImpl(long pollingPeriodMillis, long durationMillis, VerificationMode delegate, boolean returnOnSuccess)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationOverTimeImpl(long pollingPeriodMillis, long durationMillis, VerificationMode delegate, boolean returnOnSuccess)", "entityFile": "VerificationOverTimeImpl.java"} --><!-- 4fb5e79e-a231-11e9-9400-333445793454 <=< ACCEPT -->Create this verification mode, to be used to verify invocation ongoing data later.
        @param pollingPeriodMillis The frequency to poll delegate.verify(), to check whether the delegate has been satisfied
        @param durationMillis The max time to wait (in millis) for the delegate verification mode to be satisfied
        @param delegate The verification mode to delegate overall success or failure to
        @param returnOnSuccess Whether to immediately return successfully once the delegate is satisfied (as in
        org.mockito.verification.VerificationWithTimeout, or to only return once
        the delegate is satisfied and the full duration has passed (as in
        org.mockito.verification.VerificationAfterDelay).<!-- ACCEPT >=> 4fb5e79e-a231-11e9-9400-333445793454 -->

# File: `InvocationListener.java`

## Method: `void reportInvocation(MethodInvocationReport methodInvocationReport)`

        <!-- META {"entityType": "Method", "entitySignature": "void reportInvocation(MethodInvocationReport methodInvocationReport)", "entityFile": "InvocationListener.java"} -->Called after the invocation of the listener's mock if it returned normally.
        Exceptions caused by this invocationListener will raise a org.mockito.exceptions.base.MockitoException.
        @param methodInvocationReport Information about the method call that just happened.
        @see MethodInvocationReport

# File: `InvocationImpl.java`

## Class: `InvocationImpl`

        <!-- META {"entityType": "Class", "entitySignature": "InvocationImpl", "entityFile": "InvocationImpl.java"} --># Method  call on a mock object.
        Contains sequence number which should be globally unique and is used for
        verification in order.
        Contains stack trace of invocation

# File: `InvocationListener.java`

## Interface: `InvocationListener`

        <!-- META {"entityType": "Interface", "entitySignature": "InvocationListener", "entityFile": "InvocationListener.java"} -->This listener can be notified of method invocations on a mock.
        For this to happen, it must be registered using MockSettings#invocationListeners(InvocationListener...).

# File: `MethodInvocationReport.java`

## Method: `DescribedInvocation getInvocation()`

        <!-- META {"entityType": "Method", "entitySignature": "DescribedInvocation getInvocation()", "entityFile": "MethodInvocationReport.java"} -->The return type is deprecated, please assign the return value from this method
        to the DescribedInvocation type. Sorry for inconvenience but we had to move
        PrintableInvocation to better place to keep the API consistency.
        @return Information on the method call, never null

## Method: `Object getReturnedValue()`

        <!-- META {"entityType": "Method", "entitySignature": "Object getReturnedValue()", "entityFile": "MethodInvocationReport.java"} -->@return The resulting value of the method invocation, may be null

## Method: `Throwable getThrowable()`

        <!-- META {"entityType": "Method", "entitySignature": "Throwable getThrowable()", "entityFile": "MethodInvocationReport.java"} -->@return The throwable raised by the method invocation, maybe null

## Method: `boolean threwException()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean threwException()", "entityFile": "MethodInvocationReport.java"} -->@return true if an exception was raised, false otherwise

# File: `VerificationOverTimeImpl.java`

## Method: `public VerificationOverTimeImpl(long pollingPeriodMillis, VerificationMode delegate, boolean returnOnSuccess, Timer timer)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationOverTimeImpl(long pollingPeriodMillis, VerificationMode delegate, boolean returnOnSuccess, Timer timer)", "entityFile": "VerificationOverTimeImpl.java"} --><!-- 4fb5e79e-a231-11e9-9400-333445793454 <=< ACCEPT -->Create this verification mode, to be used to verify invocation ongoing data later.
        @param pollingPeriodMillis The frequency to poll delegate.verify(), to check whether the delegate has been satisfied
        @param delegate The verification mode to delegate overall success or failure to
        @param returnOnSuccess Whether to immediately return successfully once the delegate is satisfied (as in
        org.mockito.verification.VerificationWithTimeout, or to only return once
        the delegate is satisfied and the full duration has passed (as in
        org.mockito.verification.VerificationAfterDelay).
        @param timer Checker of whether the duration of the verification is still acceptable<!-- ACCEPT >=> 4fb5e79e-a231-11e9-9400-333445793454 -->

# File: `InvocationMatcher.java`

## Method: `public boolean hasSimilarMethod(Invocation candidate)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasSimilarMethod(Invocation candidate)", "entityFile": "InvocationMatcher.java"} -->similar means the same method name, same mock, unverified
        and: if arguments are the same cannot be overloaded

# File: `MethodInvocationReport.java`

## Interface: `MethodInvocationReport`

        <!-- META {"entityType": "Interface", "entitySignature": "MethodInvocationReport", "entityFile": "MethodInvocationReport.java"} -->Represent a method call on a mock.
        Contains the information on the mock, the location of the stub
        the return value if it returned something (maybe null), or an
        exception if one was thrown when the method was invoked.

# File: `VerificationOverTimeImpl.java`

## Method: `public void verify(VerificationData data)`

        <!-- META {"entityType": "Method", "entitySignature": "public void verify(VerificationData data)", "entityFile": "VerificationOverTimeImpl.java"} -->Verify the given ongoing verification data, and confirm that it satisfies the delegate verification mode
        before the full duration has passed.
        In practice, this polls the delegate verification mode until it is satisfied. If it is not satisfied once
        the full duration has passed, the last error returned by the delegate verification mode will be thrown
        here in turn. This may be thrown early if the delegate is unsatisfied and the verification mode is known
        to never recover from this situation (e.g. AtMost).
        If it is satisfied before the full duration has passed, behaviour is dependent on the returnOnSuccess parameter
        given in the constructor. If true, this verification mode is immediately satisfied once the delegate is. If
        false, this verification mode is not satisfied until the delegate is satisfied and the full time has passed.
        @throws MockitoAssertionError if the delegate verification mode does not succeed before the timeout

## Class: `VerificationOverTimeImpl`

        <!-- META {"entityType": "Class", "entitySignature": "VerificationOverTimeImpl", "entityFile": "VerificationOverTimeImpl.java"} -->Verifies that another verification mode (the delegate) is satisfied within a certain timeframe
        (before timeoutMillis has passed, measured from the call to verify()), and either returns immediately
        once it does, or waits until it is definitely satisfied once the full time has passed.

# File: `InvocationsFinder.java`

## Method: `public List<Invocation> findMatchingChunk(List<Invocation> invocations, InvocationMatcher wanted, int wantedCount, InOrderContext context)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Invocation> findMatchingChunk(List<Invocation> invocations, InvocationMatcher wanted, int wantedCount, InOrderContext context)", "entityFile": "InvocationsFinder.java"} -->some examples how it works:
        Given invocations sequence:
        1,1,2,1
        if wanted is 1 and mode is times(2) then returns
        1,1
        if wanted is 1 and mode is atLeast() then returns
        1,1,1
        if wanted is 1 and mode is times(x), where x != 2 then returns
        1,1,1

# File: `DescribedInvocation.java`

## Method: `String toString()`

        <!-- META {"entityType": "Method", "entitySignature": "String toString()", "entityFile": "DescribedInvocation.java"} -->Describes the invocation in the human friendly way.
        @return the description of this invocation.

# File: `InvocationsFinder.java`

## Method: `public Invocation findFirstUnverifiedInOrder(InOrderContext context, List<Invocation> orderedInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public Invocation findFirstUnverifiedInOrder(InOrderContext context, List<Invocation> orderedInvocations)", "entityFile": "InvocationsFinder.java"} -->i3 is unverified here:
        i1, i2, i3
        v
        all good here:
        i1, i2, i3
        v   v
        @param context
        @param orderedInvocations

# File: `DescribedInvocation.java`

## Method: `Location getLocation()`

        <!-- META {"entityType": "Method", "entitySignature": "Location getLocation()", "entityFile": "DescribedInvocation.java"} -->The place in the code where the invocation happened.
        @return the location of the invocation.

## Interface: `DescribedInvocation`

        <!-- META {"entityType": "Interface", "entitySignature": "DescribedInvocation", "entityFile": "DescribedInvocation.java"} -->Provides information about the invocation, specifically a human readable description and the location.

# File: `Invocation.java`

## Method: `boolean isVerified()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isVerified()", "entityFile": "Invocation.java"} -->@return whether the invocation has been already verified.
        Needed for org.mockito.Mockito#verifyNoMoreInteractions(Object...)

## Method: `int getSequenceNumber()`

        <!-- META {"entityType": "Method", "entitySignature": "int getSequenceNumber()", "entityFile": "Invocation.java"} -->@return the sequence number of the Invocation. Useful to determine the order of invocations.
        Used by verification in order.

## Method: `Object[] getRawArguments()`

        <!-- META {"entityType": "Method", "entitySignature": "Object[] getRawArguments()", "entityFile": "Invocation.java"} -->Returns unprocessed arguments whereas #getArguments() returns
        arguments already processed (e.g. varargs expended, etc.).
        @return unprocessed arguments, exactly as provided to this invocation.

## Method: `Class getRawReturnType()`

        <!-- META {"entityType": "Method", "entitySignature": "Class getRawReturnType()", "entityFile": "Invocation.java"} -->Returns unprocessed arguments whereas #getArguments() returns
        arguments already processed (e.g. varargs expended, etc.).
        @return unprocessed arguments, exactly as provided to this invocation.

# File: `HashCodeAndEqualsMockWrapper.java`

## Class: `HashCodeAndEqualsMockWrapper`

        <!-- META {"entityType": "Class", "entitySignature": "HashCodeAndEqualsMockWrapper", "entityFile": "HashCodeAndEqualsMockWrapper.java"} -->hashCode and equals safe mock wrapper.
        It doesn't use the actual mock Object#hashCode and Object#equals method as they might
        throw an NPE if those method cannot be stubbed even internally.
        Instead the strategy is :
        For hashCode : use System#identityHashCode
        For equals : use the object reference equality
        @see HashCodeAndEqualsSafeSet

# File: `Invocation.java`

## Method: `void markVerified()`

        <!-- META {"entityType": "Method", "entitySignature": "void markVerified()", "entityFile": "Invocation.java"} -->Marks this invocation as verified so that it will not cause verification error at
        org.mockito.Mockito#verifyNoMoreInteractions(Object...)

## Method: `StubInfo stubInfo()`

        <!-- META {"entityType": "Method", "entitySignature": "StubInfo stubInfo()", "entityFile": "Invocation.java"} -->@return the stubbing information for this invocation. May return null - this means
        the invocation was not stubbed.

## Method: `void markStubbed(StubInfo stubInfo)`

        <!-- META {"entityType": "Method", "entitySignature": "void markStubbed(StubInfo stubInfo)", "entityFile": "Invocation.java"} -->Marks this invocation as stubbed.
        @param stubInfo the information about stubbing.

## Method: `boolean isIgnoredForVerification()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isIgnoredForVerification()", "entityFile": "Invocation.java"} -->Informs if the invocation participates in verify-no-more-invocations or verification in order.
        @return whether this invocation should be ignored for the purposes of
        verify-no-more-invocations or verification in order.

## Method: `void ignoreForVerification()`

        <!-- META {"entityType": "Method", "entitySignature": "void ignoreForVerification()", "entityFile": "Invocation.java"} -->Configures this invocation to be ignored for verify-no-more-invocations or verification in order.
        See also #isIgnoredForVerification()

## Interface: `Invocation`

        <!-- META {"entityType": "Interface", "entitySignature": "Invocation", "entityFile": "Invocation.java"} -->A method call on a mock object. Contains all information and state needed for the Mockito framework to operate.
        This API might be useful for developers who extend Mockito.
        The javadoc does not have lots of examples or documentation because its audience is different.
        Vast majority of users don't need to use the Invocation. It's mostly useful for other framework authors
        that extend Mockito.
        @since 1.9.5

# File: `HashCodeAndEqualsSafeSet.java`

## Class: `HashCodeAndEqualsSafeSet`

        <!-- META {"entityType": "Class", "entitySignature": "HashCodeAndEqualsSafeSet", "entityFile": "HashCodeAndEqualsSafeSet.java"} -->hashCode and equals safe hash based set.
        Useful for holding mocks that have un-stubbable hashCode or equals method,
        meaning that in this scenario the real code is always called and will most probably
        cause an NullPointerException.
        This collection wraps the mock in an augmented type HashCodeAndEqualsMockWrapper
        that have his own implementation.
        @see HashCodeAndEqualsMockWrapper

# File: `Matchers.java`

## Method: `public static boolean anyBoolean()`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean anyBoolean()", "entityFile": "Matchers.java"} -->Any boolean or non-null Boolean
        See examples in javadoc for Matchers class
        @return false.

## Method: `public static byte anyByte()`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte anyByte()", "entityFile": "Matchers.java"} -->Any byte or non-null Byte.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static char anyChar()`

        <!-- META {"entityType": "Method", "entitySignature": "public static char anyChar()", "entityFile": "Matchers.java"} -->Any char or non-null Character.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static int anyInt()`

        <!-- META {"entityType": "Method", "entitySignature": "public static int anyInt()", "entityFile": "Matchers.java"} -->Any int or non-null Integer.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static long anyLong()`

        <!-- META {"entityType": "Method", "entitySignature": "public static long anyLong()", "entityFile": "Matchers.java"} -->Any long or non-null Long.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static float anyFloat()`

        <!-- META {"entityType": "Method", "entitySignature": "public static float anyFloat()", "entityFile": "Matchers.java"} -->Any float or non-null Float.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static double anyDouble()`

        <!-- META {"entityType": "Method", "entitySignature": "public static double anyDouble()", "entityFile": "Matchers.java"} -->Any double or non-null Double.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static short anyShort()`

        <!-- META {"entityType": "Method", "entitySignature": "public static short anyShort()", "entityFile": "Matchers.java"} -->Any short or non-null Short.
        See examples in javadoc for Matchers class
        @return 0.

## Method: `public static T anyObject()`

        <!-- META {"entityType": "Method", "entitySignature": "public static T anyObject()", "entityFile": "Matchers.java"} -->Matches anything, including null.
        This is an alias of: #any() and #any(java.lang.Class)
        See examples in javadoc for Matchers class
        @return null.

## Method: `public static T anyVararg()`

        <!-- META {"entityType": "Method", "entitySignature": "public static T anyVararg()", "entityFile": "Matchers.java"} -->Any vararg, meaning any number and values of arguments.
        Example:
        <pre class="code"><code class="java">
        //verification:
        mock.foo(1, 2);
        mock.foo(1, 2, 3, 4);
        verify(mock, times(2)).foo(anyVararg());
        //stubbing:
        when(mock.foo(anyVararg()).thenReturn(100);
        //prints 100
        System.out.println(mock.foo(1, 2));
        //also prints 100
        System.out.println(mock.foo(1, 2, 3, 4));
        See examples in javadoc for Matchers class
        @return null.

# File: `DefaultMockingDetails.java`

## Class: `DefaultMockingDetails`

        <!-- META {"entityType": "Class", "entitySignature": "DefaultMockingDetails", "entityFile": "DefaultMockingDetails.java"} --># Class  to inspect any object, and identify whether a particular object is either a mock or a spy.  This is
        a wrapper for org.mockito.internal.util.MockUtil.

# File: `Matchers.java`

## Method: `public static T any(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T any(Class<T> clazz)", "entityFile": "Matchers.java"} -->Matches any object, including nulls
        This method doesn't do type checks with the given parameter, it is only there
        to avoid casting in your code. This might however change (type checks could
        be added) in a future major release.
        See examples in javadoc for Matchers class
        This is an alias of: #any() and #anyObject()
        @return null.

## Method: `public static T any()`

        <!-- META {"entityType": "Method", "entitySignature": "public static T any()", "entityFile": "Matchers.java"} -->Matches anything, including nulls
        Shorter alias to Matchers#anyObject()
        See examples in javadoc for Matchers class
        This is an alias of: #anyObject() and #any(java.lang.Class)
        @return null.

## Method: `public static String anyString()`

        <!-- META {"entityType": "Method", "entitySignature": "public static String anyString()", "entityFile": "Matchers.java"} -->Any non-null String
        See examples in javadoc for Matchers class
        @return empty String ("")

# File: `IOUtil.java`

## Method: `public static void closeQuietly(Closeable closeable)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void closeQuietly(Closeable closeable)", "entityFile": "IOUtil.java"} -->Closes the target. Does nothing when target is null. Is silent.
        @param closeable the target, may be null

## Method: `public static void close(Closeable closeable)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void close(Closeable closeable)", "entityFile": "IOUtil.java"} -->Closes the target. Does nothing when target is null. Is not silent and exceptions are rethrown.
        @param closeable the target, may be null

## Class: `IOUtil`

        <!-- META {"entityType": "Class", "entitySignature": "IOUtil", "entityFile": "IOUtil.java"} -->IO utils. A bit of reinventing the wheel but we don't want extra dependencies at this stage and we want to be java.

# File: `Matchers.java`

## Method: `public static List anyList()`

        <!-- META {"entityType": "Method", "entitySignature": "public static List anyList()", "entityFile": "Matchers.java"} -->Any non-null List.
        See examples in javadoc for Matchers class
        @return empty List.

## Method: `public static List<T> anyListOf(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static List<T> anyListOf(Class<T> clazz)", "entityFile": "Matchers.java"} -->Generic friendly alias to Matchers#anyList().
        It's an alternative to @SuppressWarnings("unchecked") to keep code clean of compiler warnings.
        Any non-null List.
        This method doesn't do type checks with the given parameter, it is only there
        to avoid casting in your code. This might however change (type checks could
        be added) in a future major release.
        See examples in javadoc for Matchers class
        @param clazz Type owned by the list to avoid casting
        @return empty List.

## Method: `public static Set anySet()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Set anySet()", "entityFile": "Matchers.java"} -->Any non-null Set.
        See examples in javadoc for Matchers class
        @return empty Set

## Method: `public static Set<T> anySetOf(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Set<T> anySetOf(Class<T> clazz)", "entityFile": "Matchers.java"} -->Generic friendly alias to Matchers#anySet().
        It's an alternative to @SuppressWarnings("unchecked") to keep code clean of compiler warnings.
        Any non-null Set.
        This method doesn't do type checks with the given parameter, it is only there
        to avoid casting in your code. This might however change (type checks could
        be added) in a future major release.
        See examples in javadoc for Matchers class
        @param clazz Type owned by the Set to avoid casting
        @return empty Set

## Method: `public static Map anyMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Map anyMap()", "entityFile": "Matchers.java"} -->Any non-null Map.
        See examples in javadoc for Matchers class
        @return empty Map.

## Method: `public static Map<K, V> anyMapOf(Class<K> keyClazz, Class<V> valueClazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Map<K, V> anyMapOf(Class<K> keyClazz, Class<V> valueClazz)", "entityFile": "Matchers.java"} -->Generic friendly alias to Matchers#anyMap().
        It's an alternative to @SuppressWarnings("unchecked") to keep code clean of compiler warnings.
        Any non-null Map.
        This method doesn't do type checks with the given parameter, it is only there
        to avoid casting in your code. This might however change (type checks could
        be added) in a future major release.
        See examples in javadoc for Matchers class
        @param keyClazz Type of the map key to avoid casting
        @param valueClazz Type of the value to avoid casting
        @return empty Map.

## Method: `public static Collection anyCollection()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Collection anyCollection()", "entityFile": "Matchers.java"} -->Any non-null Collection.
        See examples in javadoc for Matchers class
        @return empty Collection.

# File: `GenericMetadataSupport.java`

## Method: `private BoundedType boundsOf(TypeVariable typeParameter)`

        <!-- META {"entityType": "Method", "entitySignature": "private BoundedType boundsOf(TypeVariable typeParameter)", "entityFile": "GenericMetadataSupport.java"} -->@param typeParameter The TypeVariable parameter
        @return A BoundedType for easy bound information, if first bound is a TypeVariable
        then retrieve BoundedType of this TypeVariable

## Method: `private BoundedType boundsOf(WildcardType wildCard)`

        <!-- META {"entityType": "Method", "entitySignature": "private BoundedType boundsOf(WildcardType wildCard)", "entityFile": "GenericMetadataSupport.java"} -->@param wildCard The WildCard type
        @return A BoundedType for easy bound information, if first bound is a TypeVariable
        then retrieve BoundedType of this TypeVariable

# File: `Matchers.java`

## Method: `public static Collection<T> anyCollectionOf(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Collection<T> anyCollectionOf(Class<T> clazz)", "entityFile": "Matchers.java"} -->Generic friendly alias to Matchers#anyCollection().
        It's an alternative to @SuppressWarnings("unchecked") to keep code clean of compiler warnings.
        Any non-null Collection.
        This method doesn't do type checks with the given parameter, it is only there
        to avoid casting in your code. This might however change (type checks could
        be added) in a future major release.
        See examples in javadoc for Matchers class
        @param clazz Type owned by the collection to avoid casting
        @return empty Collection.

# File: `GenericMetadataSupport.java`

## Method: `public List<Type> extraInterfaces()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Type> extraInterfaces()", "entityFile": "GenericMetadataSupport.java"} -->@return Returns extra interfaces if relevant, otherwise empty List.

## Method: `public Class<?>[] rawExtraInterfaces()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?>[] rawExtraInterfaces()", "entityFile": "GenericMetadataSupport.java"} -->@return Returns an array with the raw types of #extraInterfaces() if relevant.

## Method: `public boolean hasRawExtraInterfaces()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasRawExtraInterfaces()", "entityFile": "GenericMetadataSupport.java"} -->@return Returns true if metadata knows about extra-interfaces #extraInterfaces() if relevant.

## Method: `public Map<TypeVariable, Type> actualTypeArguments()`

        <!-- META {"entityType": "Method", "entitySignature": "public Map<TypeVariable, Type> actualTypeArguments()", "entityFile": "GenericMetadataSupport.java"} -->@return Actual type arguments matching the type variables of the raw type represented by this GenericMetadataSupport instance.

## Method: `public GenericMetadataSupport resolveGenericReturnType(Method method)`

        <!-- META {"entityType": "Method", "entitySignature": "public GenericMetadataSupport resolveGenericReturnType(Method method)", "entityFile": "GenericMetadataSupport.java"} -->Resolve current method generic return type to a GenericMetadataSupport.
        @param method Method to resolve the return type.
        @return GenericMetadataSupport representing this generic return type.

## Method: `public static GenericMetadataSupport inferFrom(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static GenericMetadataSupport inferFrom(Type type)", "entityFile": "GenericMetadataSupport.java"} -->Create an new instance of GenericMetadataSupport inferred from a Type.
        At the moment type can only be a Class or a ParameterizedType, otherwise
        it'll throw a MockitoException.
        @param type The class from which the GenericMetadataSupport should be built.
        @return The new GenericMetadataSupport.
        @throws MockitoException Raised if type is not a Class or a ParameterizedType.

## Class: `FromClassGenericMetadataSupport`

        <!-- META {"entityType": "Class", "entitySignature": "FromClassGenericMetadataSupport", "entityFile": "GenericMetadataSupport.java"} -->Generic metadata implementation for Class.
        Offer support to retrieve generic metadata on a Class by reading type parameters and type variables on
        the class and its ancestors and interfaces.

## Class: `FromParameterizedTypeGenericMetadataSupport`

        <!-- META {"entityType": "Class", "entitySignature": "FromParameterizedTypeGenericMetadataSupport", "entityFile": "GenericMetadataSupport.java"} -->Generic metadata implementation for "standalone" ParameterizedType.
        Offer support to retrieve generic metadata on a ParameterizedType by reading type variables of
        the related raw type and declared type variable of this parameterized type.
        This class is not designed to work on ParameterizedType returned by Method#getGenericReturnType(), as
        the ParameterizedType instance return in these cases could have Type Variables that refer to type declaration(s).
        That's what meant the "standalone" word at the beginning of the Javadoc.
        Instead use ParameterizedReturnType.

## Class: `ParameterizedReturnType`

        <!-- META {"entityType": "Class", "entitySignature": "ParameterizedReturnType", "entityFile": "GenericMetadataSupport.java"} -->Generic metadata specific to ParameterizedType returned via Method#getGenericReturnType().

# File: `VerboseMockInvocationLogger.java`

## Class: `VerboseMockInvocationLogger`

        <!-- META {"entityType": "Class", "entitySignature": "VerboseMockInvocationLogger", "entityFile": "VerboseMockInvocationLogger.java"} -->Logs all invocations to standard output.
        Used for debugging interactions with a mock.

# File: `Matchers.java`

## Method: `public static T isA(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T isA(Class<T> clazz)", "entityFile": "Matchers.java"} -->Object argument that implements the given class.
        See examples in javadoc for Matchers class
        @param <T>
        the accepted type.
        @param clazz
        the class of the accepted type.
        @return null.

## Method: `public static boolean eq(boolean value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean eq(boolean value)", "entityFile": "Matchers.java"} -->boolean argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static byte eq(byte value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte eq(byte value)", "entityFile": "Matchers.java"} -->byte argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static char eq(char value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char eq(char value)", "entityFile": "Matchers.java"} -->char argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static double eq(double value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double eq(double value)", "entityFile": "Matchers.java"} -->double argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static float eq(float value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float eq(float value)", "entityFile": "Matchers.java"} -->float argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static int eq(int value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int eq(int value)", "entityFile": "Matchers.java"} -->int argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

# File: `GenericMetadataSupport.java`

## Method: `public Class<?>[] rawExtraInterfaces()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?>[] rawExtraInterfaces()", "entityFile": "GenericMetadataSupport.java"} -->@return Returns an array with the extracted raw types of #extraInterfaces().
        @see #extractRawTypeOf(java.lang.reflect.Type)

## Class: `TypeVariableReturnType`

        <!-- META {"entityType": "Class", "entitySignature": "TypeVariableReturnType", "entityFile": "GenericMetadataSupport.java"} -->Generic metadata for TypeVariable returned via Method#getGenericReturnType().

## Class: `NotGenericReturnTypeSupport`

        <!-- META {"entityType": "Class", "entitySignature": "NotGenericReturnTypeSupport", "entityFile": "GenericMetadataSupport.java"} -->Non-Generic metadata for Class returned via Method#getGenericReturnType().

## Interface: `BoundedType`

        <!-- META {"entityType": "Interface", "entitySignature": "BoundedType", "entityFile": "GenericMetadataSupport.java"} -->Type representing bounds of a type
        @see TypeVarBoundedType
        @see <a href="http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4">http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4
        @see WildCardBoundedType
        @see <a href="http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.5.1">http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.5.1

## Method: `public Type firstBound()`

        <!-- META {"entityType": "Method", "entitySignature": "public Type firstBound()", "entityFile": "GenericMetadataSupport.java"} -->@return either a class or an interface (parameterized or not), if no bounds declared Object is returned.

## Method: `public Type[] interfaceBounds()`

        <!-- META {"entityType": "Method", "entitySignature": "public Type[] interfaceBounds()", "entityFile": "GenericMetadataSupport.java"} -->On a Type Variable (typeVar extends C_0 & I_1 & I_2 & etc), will return an array
        containing I_1 and I_2.
        @return other bounds for this type, these bounds can only be only interfaces as the JLS says,
        empty array if no other bound declared.

## Class: `TypeVarBoundedType`

        <!-- META {"entityType": "Class", "entitySignature": "TypeVarBoundedType", "entityFile": "GenericMetadataSupport.java"} -->Type representing bounds of a type variable, allows to keep all bounds information.
        It uses the first bound in the array, as this array is never null and always contains at least
        one element (Object is always here if no bounds are declared).
        If upper bounds are declared with SomeClass and additional interfaces, then firstBound will be SomeClass and
        interfacesBound will be an array of the additional interfaces.
        i.e. SomeClass.
        <pre class="code"><code class="java">
        interface UpperBoundedTypeWithClass<E extends Comparable<E> & Cloneable> {
        E get();
        }
        // will return Comparable type
        @see <a href="http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4">http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4

## Method: `public Type firstBound()`

        <!-- META {"entityType": "Method", "entitySignature": "public Type firstBound()", "entityFile": "GenericMetadataSupport.java"} -->@return The first bound, either a type or a reference to a TypeVariable

## Method: `public Type[] interfaceBounds()`

        <!-- META {"entityType": "Method", "entitySignature": "public Type[] interfaceBounds()", "entityFile": "GenericMetadataSupport.java"} -->@return An empty array as, wildcard don't support multiple bounds.

# File: `Primitives.java`

## Method: `public static Class<T> primitiveTypeOf(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class<T> primitiveTypeOf(Class<T> clazz)", "entityFile": "Primitives.java"} -->Returns the primitive type of the given class.
        The passed class can be any class : boolean.class, Integer.class
        in witch case this method will return boolean.class, even SomeObject.class
        in which case null will be returned.
        @param clazz The class from which primitive type has to be retrieved
        @param <T>   The type
        @return The primitive type if relevant, otherwise null

# File: `GenericMetadataSupport.java`

## Class: `WildCardBoundedType`

        <!-- META {"entityType": "Class", "entitySignature": "WildCardBoundedType", "entityFile": "GenericMetadataSupport.java"} -->Type representing bounds of a wildcard, allows to keep all bounds information.
        The JLS says that lower bound and upper bound are mutually exclusive, and that multiple bounds
        are not allowed.
        @see <a href="http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4">http://docs.oracle.com/javase/specs/jls/se5.0/html/typesValues.html#4.4

# File: `Primitives.java`

## Method: `public static boolean isPrimitiveOrWrapper(Class<?> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean isPrimitiveOrWrapper(Class<?> type)", "entityFile": "Primitives.java"} -->Indicates if the given class is primitive type or a primitive wrapper.
        @param type The type to check
        @return true if primitive or wrapper, false otherwise.

## Method: `public static T defaultValueForPrimitiveOrWrapper(Class<T> primitiveOrWrapperType)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T defaultValueForPrimitiveOrWrapper(Class<T> primitiveOrWrapperType)", "entityFile": "Primitives.java"} -->Returns the boxed default value for a primitive or a primitive wrapper.
        @param primitiveOrWrapperType The type to lookup the default value
        @return The boxed default values as defined in Java Language Specification,
        null if the type is neither a primitive nor a wrapper

# File: `Matchers.java`

## Method: `public static long eq(long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long eq(long value)", "entityFile": "Matchers.java"} -->long argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static short eq(short value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short eq(short value)", "entityFile": "Matchers.java"} -->short argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return 0.

## Method: `public static T eq(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T eq(T value)", "entityFile": "Matchers.java"} -->Object argument that is equal to the given value.
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @return null.

## Method: `public static T refEq(T value, String... excludeFields)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T refEq(T value, String... excludeFields)", "entityFile": "Matchers.java"} -->Object argument that is reflection-equal to the given value with support for excluding
        selected fields from a class.
        This matcher can be used when equals() is not implemented on compared objects.
        Matcher uses java reflection API to compare fields of wanted and actual object.
        Works similarly to EqualsBuilder.reflectionEquals(this, other, exlucdeFields) from
        apache commons library.
        Warning The equality check is shallow!
        See examples in javadoc for Matchers class
        @param value
        the given value.
        @param excludeFields
        fields to exclude, if field does not exist it is ignored.
        @return null.

## Method: `public static T same(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T same(T value)", "entityFile": "Matchers.java"} -->Object argument that is the same as the given value.
        See examples in javadoc for Matchers class
        @param <T>
        the type of the object, it is passed through to prevent casts.
        @param value
        the given value.
        @return null.

## Method: `public static Object isNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Object isNull()", "entityFile": "Matchers.java"} -->null argument.
        See examples in javadoc for Matchers class
        @return null.

# File: `GenericMetadataSupport.java`

## Class: `GenericMetadataSupport`

        <!-- META {"entityType": "Class", "entitySignature": "GenericMetadataSupport", "entityFile": "GenericMetadataSupport.java"} -->This class can retrieve generic meta-data that the compiler stores on classes
        and accessible members.
        The main idea of this code is to create a Map that will help to resolve return types.
        In order to actually work with nested generics, this map will have to be passed along new instances
        as a type context.
        Hence :
        A new instance representing the metadata is created using the #inferFrom(Type) method from a real
        # Class  or from a ParameterizedType, other types are not yet supported.
        Then from this metadata, we can extract meta-data for a generic return type of a method, using
        #resolveGenericReturnType(Method).
        For now this code support the following kind of generic declarations :
        <pre class="code"><code class="java">
        interface GenericsNest&lt;K extends Comparable&lt;K&gt; & Cloneable&gt; extends Map&lt;K, Set&lt;Number&gt;&gt; {
        Set&lt;Number&gt; remove(Object key); // override with fixed ParameterizedType
        List&lt;? super Integer&gt; returning_wildcard_with_class_lower_bound();
        List&lt;? super K&gt; returning_wildcard_with_typeVar_lower_bound();
        List&lt;? extends K&gt; returning_wildcard_with_typeVar_upper_bound();
        K returningK();
        &lt;O extends K&gt; List&lt;O&gt; paramType_with_type_params();
        &lt;S, T extends S&gt; T two_type_params();
        &lt;O extends K&gt; O typeVar_with_type_params();
        Number returningNonGeneric();
        }
        @see #inferFrom(Type)
        @see #resolveGenericReturnType(Method)
        @see org.mockito.internal.stubbing.defaultanswers.ReturnsDeepStubs

# File: `AccessibilityChanger.java`

## Method: `public void enableAccess(AccessibleObject accessibleObject)`

        <!-- META {"entityType": "Method", "entitySignature": "public void enableAccess(AccessibleObject accessibleObject)", "entityFile": "AccessibilityChanger.java"} -->changes the accessibleObject accessibility and returns true if accessibility was changed

# File: `Matchers.java`

## Method: `public static T isNull(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T isNull(Class<T> clazz)", "entityFile": "Matchers.java"} -->null argument.
        The class argument is provided to avoid casting.
        See examples in javadoc for Matchers class
        @param clazz Type to avoid casting
        @return null.

# File: `BeanPropertySetter.java`

## Method: `public BeanPropertySetter(final Object target, final Field propertyField, boolean reportNoSetterFound)`

        <!-- META {"entityType": "Method", "entitySignature": "public BeanPropertySetter(final Object target, final Field propertyField, boolean reportNoSetterFound)", "entityFile": "BeanPropertySetter.java"} -->New BeanPropertySetter
        @param target The target on which the setter must be invoked
        @param propertyField The field that should be accessed with the setter
        @param reportNoSetterFound Allow the set method to raise an Exception if the setter cannot be found

# File: `Matchers.java`

## Method: `public static Object notNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Object notNull()", "entityFile": "Matchers.java"} -->Not null argument.
        alias to Matchers#isNotNull()
        See examples in javadoc for Matchers class
        @return null.

# File: `StackTraceFilter.java`

## Method: `public StackTraceElement[] filter(StackTraceElement[] target, boolean keepTop)`

        <!-- META {"entityType": "Method", "entitySignature": "public StackTraceElement[] filter(StackTraceElement[] target, boolean keepTop)", "entityFile": "StackTraceFilter.java"} -->Example how the filter works (+/- means good/bad):
        [a+, b+, c-, d+, e+, f-, g+] -> [a+, b+, d+, e+, g+]
        Basically removes all bad from the middle.
        If any good are in the middle of bad those are also removed.

# File: `GenericTypeExtractor.java`

## Method: `public static Class genericTypeOf(Class rootClass, Class targetBaseClass, Class targetBaseInterface)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class genericTypeOf(Class rootClass, Class targetBaseClass, Class targetBaseInterface)", "entityFile": "GenericTypeExtractor.java"} -->Extract generic type of root class either from the target base class or from target base interface.
        Examples:
        1. Foo implements IFoo[Integer]:
        genericTypeOf(Foo.class, Object.class, IFoo.class) returns Integer
        2. Foo extends BaseFoo[String]:
        genericTypeOf(Foo.class, BaseFoo.class, IFoo.class) returns String
        3. Foo extends BaseFoo; BaseFoo implements IFoo[String]:
        genericTypeOf(Foo.class, BaseFoo.class, Object.class) returns String
        Does not support nested generics, only supports single type parameter.
        @param rootClass - the root class that the search begins from
        @param targetBaseClass - if one of the classes in the root class' hierarchy extends this base class
        it will be used for generic type extraction
        @param targetBaseInterface - if one of the interfaces in the root class' hierarchy implements this interface
        it will be used for generic type extraction
        @return generic interface if found, Object.class if not found.

# File: `BeanPropertySetter.java`

## Method: `public BeanPropertySetter(final Object target, final Field propertyField)`

        <!-- META {"entityType": "Method", "entitySignature": "public BeanPropertySetter(final Object target, final Field propertyField)", "entityFile": "BeanPropertySetter.java"} -->New BeanPropertySetter that don't report failure
        @param target The target on which the setter must be invoked
        @param propertyField The propertyField that must be accessed through a setter

# File: `GenericTypeExtractor.java`

## Method: `private static Type findGenericInteface(Class sourceClass, Class targetBaseInterface)`

        <!-- META {"entityType": "Method", "entitySignature": "private static Type findGenericInteface(Class sourceClass, Class targetBaseInterface)", "entityFile": "GenericTypeExtractor.java"} -->Finds generic interface implementation based on the source class and the target interface.
        Returns null if not found. Recurses the interface hierarchy.

## Method: `private static Class extractGeneric(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "private static Class extractGeneric(Type type)", "entityFile": "GenericTypeExtractor.java"} -->Attempts to extract generic parameter type of given type.
        If there is no generic parameter it returns Object.class

## Class: `GenericTypeExtractor`

        <!-- META {"entityType": "Class", "entitySignature": "GenericTypeExtractor", "entityFile": "GenericTypeExtractor.java"} -->Attempts to extract generic type of given target base class or target interface

# File: `BeanPropertySetter.java`

## Method: `public boolean set(final Object value)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean set(final Object value)", "entityFile": "BeanPropertySetter.java"} -->Set the value to the property represented by this BeanPropertySetter
        @param value the new value to pass to the property setter
        @return true if the value has been injected, false otherwise
        @throws RuntimeException Can be thrown if the setter threw an exception, if the setter is not accessible
        or, if reportNoSetterFound and setter could not be found.

## Method: `private String setterName(String fieldName)`

        <!-- META {"entityType": "Method", "entitySignature": "private String setterName(String fieldName)", "entityFile": "BeanPropertySetter.java"} -->Retrieve the setter name from the field name.
        Implementation is based on the code of java.beans.Introspector.
        @param fieldName the Field name
        @return Setter name.

## Class: `BeanPropertySetter`

        <!-- META {"entityType": "Class", "entitySignature": "BeanPropertySetter", "entityFile": "BeanPropertySetter.java"} -->This utility class will call the setter of the property to inject a new value.

# File: `Matchers.java`

## Method: `public static T notNull(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T notNull(Class<T> clazz)", "entityFile": "Matchers.java"} -->Not null argument, not necessary of the given class.
        The class argument is provided to avoid casting.
        alias to Matchers#isNotNull(Class)
        See examples in javadoc for Matchers class
        @param clazz Type to avoid casting
        @return null.

## Method: `public static Object isNotNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Object isNotNull()", "entityFile": "Matchers.java"} -->Not null argument.
        alias to Matchers#notNull()
        See examples in javadoc for Matchers class
        @return null.

## Method: `public static T isNotNull(Class<T> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T isNotNull(Class<T> clazz)", "entityFile": "Matchers.java"} -->Not null argument, not necessary of the given class.
        The class argument is provided to avoid casting.
        alias to Matchers#notNull(Class)
        See examples in javadoc for Matchers class
        @param clazz Type to avoid casting
        @return null.

# File: `Constructors.java`

## Method: `public static Constructor<?> noArgConstructorOf(Class<?> classToMock)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Constructor<?> noArgConstructorOf(Class<?> classToMock)", "entityFile": "Constructors.java"} -->Returns the no arg constructor of the type if any.
        @param classToMock The type to look for a no-arg constructor
        @return The no-arg constructor or null if none is declared.

# File: `Matchers.java`

## Method: `public static String contains(String substring)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String contains(String substring)", "entityFile": "Matchers.java"} -->String argument that contains the given substring.
        See examples in javadoc for Matchers class
        @param substring
        the substring.
        @return empty String ("").

## Method: `public static String matches(String regex)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String matches(String regex)", "entityFile": "Matchers.java"} -->String argument that matches the given regular expression.
        See examples in javadoc for Matchers class
        @param regex
        the regular expression.
        @return empty String ("").

## Method: `public static String endsWith(String suffix)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String endsWith(String suffix)", "entityFile": "Matchers.java"} -->String argument that ends with the given suffix.
        See examples in javadoc for Matchers class
        @param suffix
        the suffix.
        @return empty String ("").

## Method: `public static String startsWith(String prefix)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String startsWith(String prefix)", "entityFile": "Matchers.java"} -->String argument that starts with the given prefix.
        See examples in javadoc for Matchers class
        @param prefix
        the prefix.
        @return empty String ("").

# File: `ContainsExtraTypeInfo.java`

## Method: `String toStringWithType()`

        <!-- META {"entityType": "Method", "entitySignature": "String toStringWithType()", "entityFile": "ContainsExtraTypeInfo.java"} -->Returns more verbose description of the object which include type information

# File: `Matchers.java`

## Method: `public static T argThat(ArgumentMatcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T argThat(ArgumentMatcher<T> matcher)", "entityFile": "Matchers.java"} -->Allows creating custom argument matchers.
        This API has changed in 2.0, please read ArgumentMatcher for rationale and migration guide.
        NullPointerException auto-unboxing caveat is described below.
        It is important to understand the use cases and available options for dealing with non-trivial arguments
        before implementing custom argument matchers. This way, you can select the best possible approach
        for given scenario and produce highest quality test (clean and maintainable).
        Please read the documentation for ArgumentMatcher to learn about approaches and see the examples.
        NullPointerException auto-unboxing caveat.
        In rare cases when matching primitive parameter types you *must* use relevant intThat(), floatThat(), etc. method.
        This way you will avoid NullPointerException during auto-unboxing.
        Due to how java works we don't really have a clean way of detecting this scenario and protecting the user from this problem.
        Hopefully, the javadoc describes the problem and solution well.
        If you have an idea how to fix the problem, let us know via the mailing list or the issue tracker.
        See examples in javadoc for ArgumentMatcher class
        @param matcher decides whether argument matches
        @return null.

# File: `FieldInitializationReport.java`

## Method: `public boolean fieldWasInitialized()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean fieldWasInitialized()", "entityFile": "FieldInitializationReport.java"} -->Indicate wether the field was created during the process or not.
        @return true if created, false if the field did already hold an instance.

# File: `ContainsExtraTypeInfo.java`

## Method: `boolean typeMatches(Object target)`

        <!-- META {"entityType": "Method", "entitySignature": "boolean typeMatches(Object target)", "entityFile": "ContainsExtraTypeInfo.java"} -->Checks if target target has matching type.
        If the type matches, there is no point in rendering result from #toStringWithType()

# File: `Matchers.java`

## Method: `public static char charThat(ArgumentMatcher<Character> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char charThat(ArgumentMatcher<Character> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom char argument matchers.
        Note that #argThat will not work with primitive char matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

# File: `ContainsExtraTypeInfo.java`

## Interface: `ContainsExtraTypeInfo`

        <!-- META {"entityType": "Interface", "entitySignature": "ContainsExtraTypeInfo", "entityFile": "ContainsExtraTypeInfo.java"} -->Intended to use in certain ArgumentMatchers.
        When ArgumentMatcher fails, chance is that the actual object has the same output of toString() than
        the wanted object. This looks weird when failures are reported.
        Therefore when matcher fails but toString() yields the same outputs,
        we will try to use the #toStringWithType() method.

# File: `FieldInitializationReport.java`

## Method: `public boolean fieldWasInitializedUsingContructorArgs()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean fieldWasInitializedUsingContructorArgs()", "entityFile": "FieldInitializationReport.java"} -->Indicate wether the field was created using constructor args.
        @return true if field was created using constructor parameters.

## Method: `public Class<?> fieldClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?> fieldClass()", "entityFile": "FieldInitializationReport.java"} -->Returns the class of the actual instance in the field.
        @return Class of the instance

# File: `InstanceField.java`

## Method: `public InstanceField(Field field, Object instance)`

        <!-- META {"entityType": "Method", "entitySignature": "public InstanceField(Field field, Object instance)", "entityFile": "InstanceField.java"} -->Create a new InstanceField.
        @param field The field that should be accessed, note that no checks are performed to ensure
        the field belong to this instance class.
        @param instance The instance from which the field shall be accessed.

## Method: `public Object read()`

        <!-- META {"entityType": "Method", "entitySignature": "public Object read()", "entityFile": "InstanceField.java"} -->Safely read the field.
        @return the field value.
        @see FieldReader

# File: `Matchers.java`

## Method: `public static boolean booleanThat(ArgumentMatcher<Boolean> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean booleanThat(ArgumentMatcher<Boolean> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom boolean argument matchers.
        Note that #argThat will not work with primitive boolean matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return false.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

# File: `InstanceField.java`

## Method: `public void set(Object value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void set(Object value)", "entityFile": "InstanceField.java"} -->Set the given value to the field of this instance.
        @param value The value that should be written to the field.
        @see FieldSetter

## Method: `public boolean isNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isNull()", "entityFile": "InstanceField.java"} -->Check that the field is not null.
        @return true if null, else false.

## Method: `public boolean isAnnotatedBy(Class<? extends Annotation> annotationClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isAnnotatedBy(Class<? extends Annotation> annotationClass)", "entityFile": "InstanceField.java"} -->Check if the field is annotated by the given annotation.
        @param annotationClass The annotation type to check.
        @return true if the field is annotated by this annotation, else false.

## Method: `public boolean isSynthetic()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isSynthetic()", "entityFile": "InstanceField.java"} -->Check if the field is synthetic.
        @return true if the field is synthetic, else false.

# File: `Matchers.java`

## Method: `public static byte byteThat(ArgumentMatcher<Byte> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte byteThat(ArgumentMatcher<Byte> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom byte argument matchers.
        Note that #argThat will not work with primitive byte matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

# File: `InstanceField.java`

## Method: `public A annotation(Class<A> annotationClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public A annotation(Class<A> annotationClass)", "entityFile": "InstanceField.java"} -->Returns the annotation instance for the given annotation type.
        @param annotationClass Tha annotation type to retrieve.
        @param <A> Type of the annotation.
        @return The annotation instance.

## Method: `public Field jdkField()`

        <!-- META {"entityType": "Method", "entitySignature": "public Field jdkField()", "entityFile": "InstanceField.java"} -->Returns the JDK Field instance.
        @return The actual Field instance.

## Method: `public String name()`

        <!-- META {"entityType": "Method", "entitySignature": "public String name()", "entityFile": "InstanceField.java"} -->Returns the name of the field.
        @return Name of the field.

## Class: `InstanceField`

        <!-- META {"entityType": "Class", "entitySignature": "InstanceField", "entityFile": "InstanceField.java"} -->Represents an accessible instance field.
        Contains the instance reference on which the field can be read adn write.

# File: `Matchers.java`

## Method: `public static short shortThat(ArgumentMatcher<Short> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short shortThat(ArgumentMatcher<Short> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom short argument matchers.
        Note that #argThat will not work with primitive short matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

## Method: `public static int intThat(ArgumentMatcher<Integer> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int intThat(ArgumentMatcher<Integer> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom int argument matchers.
        Note that #argThat will not work with primitive int matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

## Method: `public static long longThat(ArgumentMatcher<Long> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long longThat(ArgumentMatcher<Long> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom long argument matchers.
        Note that #argThat will not work with primitive long matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

## Method: `public static float floatThat(ArgumentMatcher<Float> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float floatThat(ArgumentMatcher<Float> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom float argument matchers.
        Note that #argThat will not work with primitive float matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

## Method: `public static double doubleThat(ArgumentMatcher<Double> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double doubleThat(ArgumentMatcher<Double> matcher)", "entityFile": "Matchers.java"} --><!-- f9ffd5ae-1780-11ea-986d-333445793454 <=< ACCEPT -->Allows creating custom double argument matchers.
        Note that #argThat will not work with primitive double matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for Matchers class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1780-11ea-986d-333445793454 -->

# File: `FieldInitializer.java`

## Method: `public FieldInitializer(Object fieldOwner, Field field)`

        <!-- META {"entityType": "Method", "entitySignature": "public FieldInitializer(Object fieldOwner, Field field)", "entityFile": "FieldInitializer.java"} --><!-- a0cbcde6-1781-11ea-a114-333445793454 <=< ACCEPT -->Prepare initializer with the given field on the given instance.
        This constructor fail fast if the field type cannot be handled.
        @param fieldOwner Instance of the test.
        @param field Field to be initialize.<!-- ACCEPT >=> a0cbcde6-1781-11ea-a114-333445793454 -->

## Method: `public FieldInitializer(Object fieldOwner, Field field, ConstructorArgumentResolver argResolver)`

        <!-- META {"entityType": "Method", "entitySignature": "public FieldInitializer(Object fieldOwner, Field field, ConstructorArgumentResolver argResolver)", "entityFile": "FieldInitializer.java"} --><!-- a0cbcde6-1781-11ea-a114-333445793454 <=< ACCEPT -->Prepare initializer with the given field on the given instance.
        This constructor fail fast if the field type cannot be handled.
        @param fieldOwner Instance of the test.
        @param field Field to be initialize.
        @param argResolver Constructor parameters resolver<!-- ACCEPT >=> a0cbcde6-1781-11ea-a114-333445793454 -->

## Method: `public FieldInitializationReport initialize()`

        <!-- META {"entityType": "Method", "entitySignature": "public FieldInitializationReport initialize()", "entityFile": "FieldInitializer.java"} -->Initialize field if not initialized and return the actual instance.
        @return Actual field instance.

# File: `SuperTypesLastSorter.java`

## Method: `public List<Field> sort(Collection<? extends Field> unsortedFields)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Field> sort(Collection<? extends Field> unsortedFields)", "entityFile": "SuperTypesLastSorter.java"} -->Return a new collection with the fields sorted first by name,
        then with any fields moved after their supertypes.

# File: `Matchers.java`

## Class: `Matchers`

        <!-- META {"entityType": "Class", "entitySignature": "Matchers", "entityFile": "Matchers.java"} -->Allow flexible verification or stubbing. See also AdditionalMatchers.
        Mockito extends Matchers so to get access to all matchers just import Mockito class statically.
        <pre class="code"><code class="java">
        //stubbing using anyInt() argument matcher
        when(mockedList.get(anyInt())).thenReturn("element");
        //following prints "element"
        System.out.println(mockedList.get(999));
        //you can also verify using argument matcher
        verify(mockedList).get(anyInt());
        Scroll down to see all methods - full list of matchers.
        Warning:
        If you are using argument matchers, all arguments have to be provided by matchers.
        E.g: (example shows verification but the same applies to stubbing):
        <pre class="code"><code class="java">
        verify(mock).someMethod(anyInt(), anyString(), eq("third argument"));
        //above is correct - eq() is also an argument matcher
        verify(mock).someMethod(anyInt(), anyString(), "third argument");
        //above is incorrect - exception will be thrown because third argument is given without argument matcher.
        Matcher methods like anyObject(), eq() do not return matchers.
        Internally, they record a matcher on a stack and return a dummy value (usually null).
        This implementation is due static type safety imposed by java compiler.
        The consequence is that you cannot use anyObject(), eq() methods outside of verified/stubbed method.
        Custom Argument Matchers
        It is important to understand the use cases and available options for dealing with non-trivial arguments
        before implementing custom argument matchers. This way, you can select the best possible approach
        for given scenario and produce highest quality test (clean and maintainable).
        Please read on in the javadoc for ArgumentMatcher to learn about approaches and see the examples.

# File: `SuperTypesLastSorter.java`

## Class: `SuperTypesLastSorter`

        <!-- META {"entityType": "Class", "entitySignature": "SuperTypesLastSorter", "entityFile": "SuperTypesLastSorter.java"} -->Sort fields in an order suitable for injection, by name with superclasses
        moved after their subclasses.

# File: `FieldInitializer.java`

## Method: `Object[] resolveTypeInstances(Class<?>... argTypes)`

        <!-- META {"entityType": "Method", "entitySignature": "Object[] resolveTypeInstances(Class<?>... argTypes)", "entityFile": "FieldInitializer.java"} -->Try to resolve instances from types.
        Checks on the real argument type or on the correct argument number
        will happen during the field initialization FieldInitializer#initialize().
        I.e the only responsibility of this method, is to provide instances if possible.
        @param argTypes Constructor argument types, should not be null.
        @return The argument instances to be given to the constructor, should not be null.

# File: `RemoveFirstLine.java`

## Method: `public String of(String text)`

        <!-- META {"entityType": "Method", "entitySignature": "public String of(String text)", "entityFile": "RemoveFirstLine.java"} -->@param text to have the first line removed
        @return less first line

# File: `FieldInitializer.java`

## Interface: `ConstructorArgumentResolver`

        <!-- META {"entityType": "Interface", "entitySignature": "ConstructorArgumentResolver", "entityFile": "FieldInitializer.java"} -->Represents the strategy used to resolve actual instances
        to be given to a constructor given the argument types.

## Method: `NoArgConstructorInstantiator(Object testClass, Field field)`

        <!-- META {"entityType": "Method", "entitySignature": "NoArgConstructorInstantiator(Object testClass, Field field)", "entityFile": "FieldInitializer.java"} -->Internal, checks are done by FieldInitializer.
        Fields are assumed to be accessible.

# File: `MockCreationSettings.java`

## Method: `Class<T> getTypeToMock()`

        <!-- META {"entityType": "Method", "entitySignature": "Class<T> getTypeToMock()", "entityFile": "MockCreationSettings.java"} -->Mocked type. An interface or class the mock should implement / extend.

## Method: `MockName getMockName()`

        <!-- META {"entityType": "Method", "entitySignature": "MockName getMockName()", "entityFile": "MockCreationSettings.java"} -->the name of this mock, as printed on verification errors; see org.mockito.MockSettings#name.

## Method: `Answer getDefaultAnswer()`

        <!-- META {"entityType": "Method", "entitySignature": "Answer getDefaultAnswer()", "entityFile": "MockCreationSettings.java"} -->the default answer for this mock, see org.mockito.MockSettings#defaultAnswer.

## Method: `boolean isSerializable()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isSerializable()", "entityFile": "MockCreationSettings.java"} -->if the mock is serializable, see org.mockito.MockSettings#serializable.

## Method: `boolean isStubOnly()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isStubOnly()", "entityFile": "MockCreationSettings.java"} -->Whether the mock is only for stubbing, i.e. does not remember
        parameters on its invocation and therefore cannot
        be used for verification

## Method: `List<InvocationListener> getInvocationListeners()`

        <!-- META {"entityType": "Method", "entitySignature": "List<InvocationListener> getInvocationListeners()", "entityFile": "MockCreationSettings.java"} -->The invocation listeners attached to this mock, see org.mockito.MockSettings#invocationListeners.

# File: `FieldInitializer.java`

## Class: `NoArgConstructorInstantiator`

        <!-- META {"entityType": "Class", "entitySignature": "NoArgConstructorInstantiator", "entityFile": "FieldInitializer.java"} -->Constructor instantiating strategy for no-arg constructor.
        If a no-arg constructor can be found then the instance is created using
        this constructor.
        Otherwise a technical MockitoException is thrown.

# File: `MockCreationSettings.java`

## Method: `boolean isUsingConstructor()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isUsingConstructor()", "entityFile": "MockCreationSettings.java"} -->Informs whether the mock instance should be created via constructor
        @since 1.10.12

# File: `FieldInitializer.java`

## Method: `ParameterizedConstructorInstantiator(Object testClass, Field field, ConstructorArgumentResolver argumentResolver)`

        <!-- META {"entityType": "Method", "entitySignature": "ParameterizedConstructorInstantiator(Object testClass, Field field, ConstructorArgumentResolver argumentResolver)", "entityFile": "FieldInitializer.java"} -->Internal, checks are done by FieldInitializer.
        Fields are assumed to be accessible.

# File: `MockCreationSettings.java`

## Method: `Object getOuterClassInstance()`

        <!-- META {"entityType": "Method", "entitySignature": "Object getOuterClassInstance()", "entityFile": "MockCreationSettings.java"} -->Used when mocking non-static inner classes in conjunction with #isUsingConstructor()
        @return the outer class instance used for creation of the mock object via the constructor.
        @since 1.10.12

# File: `FieldInitializer.java`

## Class: `ParameterizedConstructorInstantiator`

        <!-- META {"entityType": "Class", "entitySignature": "ParameterizedConstructorInstantiator", "entityFile": "FieldInitializer.java"} -->Constructor instantiating strategy for parameterized constructors.
        Choose the constructor with the highest number of parameters, then
        call the ConstructorArgResolver to get actual argument instances.
        If the argResolver fail, then a technical MockitoException is thrown is thrown.
        Otherwise the instance is created with the resolved arguments.

# File: `FriendlyExceptionMaker.java`

## Class: `FriendlyExceptionMaker`

        <!-- META {"entityType": "Class", "entitySignature": "FriendlyExceptionMaker", "entityFile": "FriendlyExceptionMaker.java"} -->If JUnit is used, we can use an exception that extends from ComparisonFailure
        and hence provide a better IDE support as the comparison result is comparable

# File: `MockCreationSettings.java`

## Interface: `MockCreationSettings`

        <!-- META {"entityType": "Interface", "entitySignature": "MockCreationSettings", "entityFile": "MockCreationSettings.java"} -->Informs about the mock settings. An immutable view of org.mockito.MockSettings.

# File: `FieldInitializer.java`

## Class: `FieldInitializer`

        <!-- META {"entityType": "Class", "entitySignature": "FieldInitializer", "entityFile": "FieldInitializer.java"} -->Initialize a field with type instance if a default constructor can be found.
        If the given field is already initialized, then the actual instance is returned.
        This initializer doesn't work with inner classes, local classes, interfaces or abstract types.

# File: `MockName.java`

## Method: `boolean isDefault()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isDefault()", "entityFile": "MockName.java"} -->default name means generated by Mockito. non-default means the user has named the mock at creation.

## Interface: `MockName`

        <!-- META {"entityType": "Interface", "entitySignature": "MockName", "entityFile": "MockName.java"} -->Represents the name of the mock as shown in the verification failure reports, etc.

# File: `SerializableMode.java`

## EnumConstant: `BASIC`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "BASIC", "entityFile": "SerializableMode.java"} -->Basic serializable mode for mock objects. Introduced in Mockito 1.8.1.

## EnumConstant: `ACROSS_CLASSLOADERS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "ACROSS_CLASSLOADERS", "entityFile": "SerializableMode.java"} -->Useful if the mock is deserialized in a different classloader / vm.

# File: `NotifiedMethodInvocationReport.java`

## Method: `public NotifiedMethodInvocationReport(Invocation invocation, Object returnedValue)`

        <!-- META {"entityType": "Method", "entitySignature": "public NotifiedMethodInvocationReport(Invocation invocation, Object returnedValue)", "entityFile": "NotifiedMethodInvocationReport.java"} --><!-- ff8fd3b4-1781-11ea-8b13-333445793454 <=< ACCEPT -->Build a new org.mockito.listeners.MethodInvocationReport with a return value.
        @param invocation Information on the method call
        @param returnedValue The value returned by the method invocation<!-- ACCEPT >=> ff8fd3b4-1781-11ea-8b13-333445793454 -->

## Method: `public NotifiedMethodInvocationReport(Invocation invocation, Throwable throwable)`

        <!-- META {"entityType": "Method", "entitySignature": "public NotifiedMethodInvocationReport(Invocation invocation, Throwable throwable)", "entityFile": "NotifiedMethodInvocationReport.java"} --><!-- ff8fd3b4-1781-11ea-8b13-333445793454 <=< ACCEPT -->Build a new org.mockito.listeners.MethodInvocationReport with a return value.
        @param invocation Information on the method call
        @param throwable Tha throwable raised by the method invocation<!-- ACCEPT >=> ff8fd3b4-1781-11ea-8b13-333445793454 -->

# File: `ArgumentMatchingTool.java`

## Method: `public Integer[] getSuspiciouslyNotMatchingArgsIndexes(List<ArgumentMatcher> matchers, Object[] arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public Integer[] getSuspiciouslyNotMatchingArgsIndexes(List<ArgumentMatcher> matchers, Object[] arguments)", "entityFile": "ArgumentMatchingTool.java"} -->Suspiciously not matching arguments are those that don't match, the toString() representation is the same but types are different.

# File: `Mock.java`

## Annotation: `Mock`

        <!-- META {"entityType": "Annotation", "entitySignature": "Mock", "entityFile": "Mock.java"} -->Mark a field as a mock.
        Allows shorthand mock creation.
        Minimizes repetitive mock creation code.
        Makes the test class more readable.
        Makes the verification error easier to read because the field name is used to identify the mock.
        <pre class="code"><code class="java">
        public class ArticleManagerTest extends SampleBaseTestCase {
        @Mock private ArticleCalculator calculator;
        @Mock(name = "database") private ArticleDatabase dbMock;
        @Mock(answer = RETURNS_MOCKS) private UserProvider userProvider;
        @Mock(extraInterfaces = {Queue.class, Observer.class}) private  articleMonitor;
        private ArticleManager manager;
        @Before public void setup() {
        manager = new ArticleManager(userProvider, database, calculator, articleMonitor);
        }
        }
        public class SampleBaseTestCase {
        @Before public void initMocks() {
        MockitoAnnotations.initMocks(this);
        }
        }
        MockitoAnnotations.initMocks(this) method has to be called to initialize annotated objects.
        In above example, initMocks() is called in @Before (JUnit4) method of test's base class.
        For JUnit3 initMocks() can go to setup() method of a base class.
        Instead you can also put initMocks() in your JUnit runner (@RunWith) or use the built-in
        org.mockito.runners.MockitoJUnitRunner.
        @see Mockito#mock(Class)
        @see Spy
        @see InjectMocks
        @see MockitoAnnotations#initMocks(Object)
        @see org.mockito.runners.MockitoJUnitRunner

# File: `Fields.java`

## Method: `public static InstanceFields allDeclaredFieldsOf(Object instance)`

        <!-- META {"entityType": "Method", "entitySignature": "public static InstanceFields allDeclaredFieldsOf(Object instance)", "entityFile": "Fields.java"} -->Instance fields declared in the class and superclasses of the given instance.
        @param instance Instance from which declared fields will be retrieved.
        @return InstanceFields of this object instance.

# File: `MockingDetails.java`

## Method: `boolean isMock()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isMock()", "entityFile": "MockingDetails.java"} -->Informs if the object is a mock. isMock() for null input returns false.
        @return true if the object is a mock or a spy.
        @since 1.9.5

# File: `Fields.java`

## Method: `public static InstanceFields declaredFieldsOf(Object instance)`

        <!-- META {"entityType": "Method", "entitySignature": "public static InstanceFields declaredFieldsOf(Object instance)", "entityFile": "Fields.java"} -->Instance fields declared in the class of the given instance.
        @param instance Instance from which declared fields will be retrieved.
        @return InstanceFields of this object instance.

# File: `MockingDetails.java`

## Method: `boolean isSpy()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isSpy()", "entityFile": "MockingDetails.java"} -->Informs if the object is a spy. isSpy() for null input returns false.
        @return true if the object is a spy.
        @since 1.9.5

# File: `Fields.java`

## Method: `public static Filter<InstanceField> annotatedBy(final Class<? extends Annotation>... annotations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Filter<InstanceField> annotatedBy(final Class<? extends Annotation>... annotations)", "entityFile": "Fields.java"} -->Accept fields annotated by the given annotations.
        @param annotations Annotation types to check.
        @return The filter.

# File: `MockingDetails.java`

## Method: `Collection<Invocation> getInvocations()`

        <!-- META {"entityType": "Method", "entitySignature": "Collection<Invocation> getInvocations()", "entityFile": "MockingDetails.java"} -->Provides a collection of methods indicating the invocations of the object
        @return collection of Invocation representing the invocations
        for the object.
        @since 1.10.0

## Method: `Class<?> getMockedType()`

        <!-- META {"entityType": "Method", "entitySignature": "Class<?> getMockedType()", "entityFile": "MockingDetails.java"} -->Returns the type that is mocked. It is the type originally passed to
        the Mockito#mock(Class) or Mockito#spy(Class) function,
        or the type referenced by a Mockito annotation.
        @return The mocked type
        @since 2.0.0

# File: `Fields.java`

## Class: `Fields`

        <!-- META {"entityType": "Class", "entitySignature": "Fields", "entityFile": "Fields.java"} -->Small fluent reflection tools to work with fields.
        Code is very new and might need rework.

# File: `MockingDetails.java`

## Method: `Set<Class> getExtraInterfaces()`

        <!-- META {"entityType": "Method", "entitySignature": "Set<Class> getExtraInterfaces()", "entityFile": "MockingDetails.java"} -->Returns the extra-interfaces of the mock. The interfaces that were configured at the mock creation
        with the MockSettings#extraInterfaces(Class[]).
        @return The extra-interfaces
        @since 2.0.0

## Interface: `MockingDetails`

        <!-- META {"entityType": "Interface", "entitySignature": "MockingDetails", "entityFile": "MockingDetails.java"} -->Provides mocking information.
        For example, you can identify whether a particular object is either a mock or a spy.
        @since 1.9.5

# File: `GenericMaster.java`

## Method: `public Class getGenericType(Field field)`

        <!-- META {"entityType": "Method", "entitySignature": "public Class getGenericType(Field field)", "entityFile": "GenericMaster.java"} -->Finds the generic type (parametrized type) of the field. If the field is not generic it returns Object.class.
        @param field

# File: `RunnerImpl.java`

## Interface: `RunnerImpl`

        <!-- META {"entityType": "Interface", "entitySignature": "RunnerImpl", "entityFile": "RunnerImpl.java"} -->I'm using this surrogate interface to hide internal Runner implementations.
        Surrogate cannot be used with @RunWith therefore it is less likely clients will use interal runners.

# File: `InstantiatorProvider.java`

## Interface: `InstantiatorProvider`

        <!-- META {"entityType": "Interface", "entitySignature": "InstantiatorProvider", "entityFile": "InstantiatorProvider.java"} -->Mockito will invoke this interface in order to fetch an instance instantiator provider.
        By default, an internal byte-buddy/asm/objenesis based implementation is used.
        Using the extension point
        The plugin mechanism of mockito works in a similar way as the
        java.util.ServiceLoader, however instead of looking in the META-INF
        directory, Mockito will look in mockito-extensions directory.
        The reason for that is that Android SDK strips jar from the META-INF
        directory when creating an APK.
        <ol style="list-style-type: lower-alpha">
        The implementation itself, for example
        org.awesome.mockito.AwesomeInstantiatorProvider that implements the
        InstantiatorProvider.
        A file "mockito-extensions/org.mockito.plugins.InstantiatorProvider".
        The content of this file is exactly a one line with the qualified
        name: org.awesome.mockito.AwesomeInstantiatorProvider.
        Note that if several mockito-extensions/org.mockito.plugins.InstantiatorProvider
        files exists in the classpath, Mockito will only use the first returned by the standard
        ClassLoader#getResource mechanism.
        So just create a custom implementation of InstantiatorProvider and place the
        qualified name in the following file
        mockito-extensions/org.mockito.plugins.InstantiatorProvider.
        @since 21.10.15

# File: `MockMaker.java`

## Method: `T createMock(MockCreationSettings<T> settings, MockHandler handler)`

        <!-- META {"entityType": "Method", "entitySignature": "T createMock(MockCreationSettings<T> settings, MockHandler handler)", "entityFile": "MockMaker.java"} -->If you want to provide your own implementation of MockMaker this method should:
        Create a proxy object that implements settings.typeToMock and potentially also settings.extraInterfaces.
        You may use the information from settings to create/configure your proxy object.
        Your proxy object should carry the handler with it. For example, if you generate byte code
        to create the proxy you could generate an extra field to keep the handler with the generated object.
        Your implementation of MockMaker is required to provide this instance of handler when
        #getHandler(Object) is called.
        @param settings Mock creation settings like type to mock, extra interfaces and so on.
        @param handler See org.mockito.invocation.MockHandler.
        Do not provide your own implementation at this time. Make sure your implementation of
        #getHandler(Object) will return this instance.
        @param <T> Type of the mock to return, actually the settings.getTypeToMock.
        @return The mock instance.
        @since 1.9.5

# File: `CallsRealMethods.java`

## Class: `CallsRealMethods`

        <!-- META {"entityType": "Class", "entitySignature": "CallsRealMethods", "entityFile": "CallsRealMethods.java"} --><!-- 305f42d4-1781-11ea-8400-333445793454 <=< ACCEPT -->Optional Answer that adds partial mocking support
        Answer can be used to define the return values of unstubbed invocations.
        This implementation can be helpful when working with legacy code.
        When this implementation is used, unstubbed methods will delegate to the real implementation.
        This is a way to create a partial mock object that calls real methods by default.
        As usual you are going to read the partial mock warning:
        Object oriented programming is more less tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.<!-- ACCEPT >=> 305f42d4-1781-11ea-8400-333445793454 -->

# File: `MockMaker.java`

## Method: `MockHandler getHandler(Object mock)`

        <!-- META {"entityType": "Method", "entitySignature": "MockHandler getHandler(Object mock)", "entityFile": "MockMaker.java"} -->Returns the handler for the mock. Do not provide your own implementations at this time
        because the work on the MockHandler api is not completed.
        Use the instance provided to you by Mockito at #createMock or #resetMock.
        @param mock The mock instance.
        @return The mock handler, but may return null - it means that there is no handler attached to provided object.
        This means the passed object is not really a Mockito mock.
        @since 1.9.5

# File: `Mockito.java`

## Field: `RETURNS_DEFAULTS`

        <!-- META {"entityType": "Field", "entitySignature": "RETURNS_DEFAULTS", "entityFile": "Mockito.java"} -->The default Answer of every mock if the mock was not stubbed.
        Typically it just returns some empty value.
        Answer can be used to define the return values of unstubbed invocations.
        This implementation first tries the global configuration.
        If there is no global configuration then it uses ReturnsEmptyValues (returns zeros, empty collections, nulls, etc.)

# File: `EqualsBuilder.java`

## Field: `isEquals`

        <!-- META {"entityType": "Field", "entitySignature": "isEquals", "entityFile": "EqualsBuilder.java"} -->If the fields tested are equals.
        The default value is true.

# File: `MockMaker.java`

## Method: `void resetMock(Object mock, MockHandler newHandler, MockCreationSettings settings)`

        <!-- META {"entityType": "Method", "entitySignature": "void resetMock(Object mock, MockHandler newHandler, MockCreationSettings settings)", "entityFile": "MockMaker.java"} -->Replaces the existing handler on mock with newHandler.
        The invocation handler actually store invocations to achieve
        stubbing and verification. In order to reset the mock, we pass
        a new instance of the invocation handler.
        Your implementation should make sure the newHandler is correctly associated to passed mock
        @param mock The mock instance whose invocation handler is to be replaced.
        @param newHandler The new invocation handler instance.
        @param settings The mock settings - should you need to access some of the mock creation details.
        @since 1.9.5

# File: `Mockito.java`

## Field: `RETURNS_SMART_NULLS`

        <!-- META {"entityType": "Field", "entitySignature": "RETURNS_SMART_NULLS", "entityFile": "Mockito.java"} --><!-- 36fc2376-a231-11e9-87a8-333445793454 <=< ACCEPT -->Optional Answer to be used with Mockito#mock(Class, Answer).
        Answer can be used to define the return values of unstubbed invocations.
        This implementation can be helpful when working with legacy code.
        Unstubbed methods often return null. If your code uses the object returned by an unstubbed call you get a NullPointerException.
        This implementation of Answer returns SmartNull instead of null.
        SmartNull gives nicer exception message than NPE because it points out the line where unstubbed method was called. You just click on the stack trace.
        ReturnsSmartNulls first tries to return ordinary return values (see ReturnsMoreEmptyValues)
        then it tries to return SmartNull. If the return type is final then plain null is returned.
        ReturnsSmartNulls will be probably the default return values strategy in Mockito 2.0.
        Example:
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, RETURNS_SMART_NULLS);
        //calling unstubbed method here:
        Stuff stuff = mock.getStuff();
        //using object returned by unstubbed call:
        stuff.doSomething();
        //Above doesn't yield NullPointerException this time!
        //Instead, SmartNullPointerException is thrown.
        //Exception's cause links to unstubbed mock.getStuff() - just click on the stack trace.
        <!-- ACCEPT >=> 36fc2376-a231-11e9-87a8-333445793454 -->

# File: `ReturnsArgumentAt.java`

## Method: `public ReturnsArgumentAt(int wantedArgumentPosition)`

        <!-- META {"entityType": "Method", "entitySignature": "public ReturnsArgumentAt(int wantedArgumentPosition)", "entityFile": "ReturnsArgumentAt.java"} -->Build the identity answer to return the argument at the given position in the argument array.
        @param wantedArgumentPosition The position of the argument identity to return in the invocation.
        Using -1 indicates the last argument.

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder()`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder()", "entityFile": "EqualsBuilder.java"} -->Constructor for EqualsBuilder.
        Starts off assuming that equals is true.
        @see Object#equals(Object)

# File: `MockMaker.java`

## Method: `TypeMockability isTypeMockable(Class<?> type)`

        <!-- META {"entityType": "Method", "entitySignature": "TypeMockability isTypeMockable(Class<?> type)", "entityFile": "MockMaker.java"} -->Indicates if the given type can be mocked by this mockmaker.
        Mockmaker may have different capabilities in term of mocking, typically
        Mockito 1.x's internal mockmaker cannot mock final types. Other implementations, may
        have different limitations.
        @param type The type inspected for mockability.
        @return object that carries the information about mockability of given type.
        @since 2.0

# File: `Mockito.java`

## Field: `RETURNS_MOCKS`

        <!-- META {"entityType": "Field", "entitySignature": "RETURNS_MOCKS", "entityFile": "Mockito.java"} -->Optional Answer to be used with Mockito#mock(Class, Answer)
        Answer can be used to define the return values of unstubbed invocations.
        This implementation can be helpful when working with legacy code.
        ReturnsMocks first tries to return ordinary return values (see ReturnsMoreEmptyValues)
        then it tries to return mocks. If the return type cannot be mocked (e.g. is final) then plain null is returned.

# File: `ReturnsArgumentAt.java`

## Class: `ReturnsArgumentAt`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsArgumentAt", "entityFile": "ReturnsArgumentAt.java"} -->Returns the passed parameter identity at specified index.
        The argumentIndex represents the index in the argument array of the invocation.
        If this number equals -1 then the last argument is returned.
        @see org.mockito.AdditionalAnswers
        @since 1.9.5

# File: `ReturnsElementsOf.java`

## Class: `ReturnsElementsOf`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsElementsOf", "entityFile": "ReturnsElementsOf.java"} --><!-- 62e3dc36-1785-11ea-bbed-333445793454 <=< ACCEPT -->Returns elements of the collection. Keeps returning the last element forever.
        Might be useful on occasion when you have a collection of elements to return.
        <pre class="code"><code class="java">
        //this:
        when(mock.foo()).thenReturn(1, 2, 3);
        //is equivalent to:
        when(mock.foo()).thenAnswer(new ReturnsElementsOf(Arrays.asList(1, 2, 3)));
        Also you might better want to use the static factory there
        org.mockito.AdditionalAnswers#returnsElementsOf(java.util.Collection)
        @see org.mockito.AdditionalAnswers<!-- ACCEPT >=> 62e3dc36-1785-11ea-bbed-333445793454 -->

# File: `EqualsBuilder.java`

## Method: `public static boolean reflectionEquals(Object lhs, Object rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean reflectionEquals(Object lhs, Object rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 29f444ee-1782-11ea-a04a-333445793454 <=< ACCEPT -->This method uses reflection to determine if the two Objects
        are equal.
        It uses AccessibleObject.setAccessible to gain access to private
        fields. This means that it will throw a security exception if run under
        a security manager, if the permissions are not set up correctly. It is also
        not as efficient as testing explicitly.
        Transient members will be not be tested, as they are likely derived
        fields, and not part of the value of the Object.
        Static fields will not be tested. Superclass fields will be included.
        @param lhs  this object
        @param rhs  the other object
        @return true if the two Objects have tested equals.<!-- ACCEPT >=> 29f444ee-1782-11ea-a04a-333445793454 -->

# File: `MockMaker.java`

## Interface: `MockMaker`

        <!-- META {"entityType": "Interface", "entitySignature": "MockMaker", "entityFile": "MockMaker.java"} -->The facility to create mocks.
        By default, an internal byte-buddy/asm/objenesis based implementation is used.
        MockMaker is an extension point that makes it possible to use custom dynamic proxies
        and avoid using the default byte-buddy/asm/objenesis implementation.
        For example, the android users can use a MockMaker that can work with Dalvik virtual machine
        and hence bring Mockito to android apps developers.
        Using the extension point
        Suppose you wrote an extension to create mocks with some Awesome library, in order to tell
        Mockito to use it you need to put in your classpath:
        <ol style="list-style-type: lower-alpha">
        The implementation itself, for example org.awesome.mockito.AwesomeMockMaker that
        extends the MockMaker.
        A file "mockito-extensions/org.mockito.plugins.MockMaker". The content of this file is
        exactly a one line with the qualified name:
        org.awesome.mockito.AwesomeMockMaker.
        *
        Note that if several mockito-extensions/org.mockito.plugins.MockMaker files exists in the classpath
        Mockito will only use the first returned by the standard ClassLoader#getResource mechanism.
        @see org.mockito.mock.MockCreationSettings
        @see org.mockito.invocation.MockHandler
        @since 1.9.5

# File: `EqualsBuilder.java`

## Method: `public static boolean reflectionEquals(Object lhs, Object rhs, String[] excludeFields)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean reflectionEquals(Object lhs, Object rhs, String[] excludeFields)", "entityFile": "EqualsBuilder.java"} --><!-- 29f444ee-1782-11ea-a04a-333445793454 <=< ACCEPT -->This method uses reflection to determine if the two Objects
        are equal.
        It uses AccessibleObject.setAccessible to gain access to private
        fields. This means that it will throw a security exception if run under
        a security manager, if the permissions are not set up correctly. It is also
        not as efficient as testing explicitly.
        Transient members will be not be tested, as they are likely derived
        fields, and not part of the value of the Object.
        Static fields will not be tested. Superclass fields will be included.
        @param lhs  this object
        @param rhs  the other object
        @param excludeFields  array of field names to exclude from testing
        @return true if the two Objects have tested equals.<!-- ACCEPT >=> 29f444ee-1782-11ea-a04a-333445793454 -->

# File: `PluginSwitch.java`

## Method: `boolean isEnabled(String pluginClassName)`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isEnabled(String pluginClassName)", "entityFile": "PluginSwitch.java"} -->Mockito invokes this method for every plugin found in the classpath
        (except from the PluginSwitch implementation itself).
        If no custom plugins are discovered this method is not invoked.
        @since 1.10.15

# File: `EqualsBuilder.java`

## Method: `public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients)", "entityFile": "EqualsBuilder.java"} --><!-- 29f444ee-1782-11ea-a04a-333445793454 <=< ACCEPT -->This method uses reflection to determine if the two Objects
        are equal.
        It uses AccessibleObject.setAccessible to gain access to private
        fields. This means that it will throw a security exception if run under
        a security manager, if the permissions are not set up correctly. It is also
        not as efficient as testing explicitly.
        If the TestTransients parameter is set to true, transient
        members will be tested, otherwise they are ignored, as they are likely
        derived fields, and not part of the value of the Object.
        Static fields will not be tested. Superclass fields will be included.
        @param lhs  this object
        @param rhs  the other object
        @param testTransients  whether to include transient fields
        @return true if the two Objects have tested equals.<!-- ACCEPT >=> 29f444ee-1782-11ea-a04a-333445793454 -->

# File: `PluginSwitch.java`

## Interface: `PluginSwitch`

        <!-- META {"entityType": "Interface", "entitySignature": "PluginSwitch", "entityFile": "PluginSwitch.java"} -->Allows switching off the plugins that are discovered on classpath.
        Mockito will invoke this interface in order to select whether a plugin is enabled or not.
        When a particular plugin is switched off, the default Mockito behavior is used.
        For example, if Android's dexmaker MockMaker is switched off,
        Mockito default MockMaker implementation is used org.mockito.plugins.MockMaker
        Using the extension point
        The plugin mechanism of mockito works in a similar way as the java.util.ServiceLoader, however instead of
        looking in the META-INF directory, Mockito will look in mockito-extensions directory.
        The reason for that is that Android SDK strips jar from the META-INF directory when creating an APK.
        <ol style="list-style-type: lower-alpha">
        The implementation itself, for example org.awesome.mockito.AwesomeMockMaker that extends the MockMaker.
        A file "mockito-extensions/org.mockito.plugins.MockMaker". The content of this file is
        exactly a one line with the qualified name: org.awesome.mockito.AwesomeMockMaker.
        Note that if several mockito-extensions/org.mockito.plugins.MockMaker files exists in the classpath
        Mockito will only use the first returned by the standard ClassLoader#getResource mechanism.
        So just create a custom implementation of PluginSwitch and place the qualified name in the following file
        mockito-extensions/org.mockito.plugins.PluginSwitch.
        @since 1.10.15

# File: `Answers.java`

## Enum: `Answers`

        <!-- META {"entityType": "Enum", "entitySignature": "Answers", "entityFile": "Answers.java"} -->Enumeration of pre-configured mock answers
        @deprecated - please use Answers from top Mockito package: org.mockito.Answers
        WARNING Those answers no longer are used by the framework!!! Please use org.mockito.Answers
        See Mockito for more information.

# File: `Mockito.java`

## Field: `RETURNS_DEEP_STUBS`

        <!-- META {"entityType": "Field", "entitySignature": "RETURNS_DEEP_STUBS", "entityFile": "Mockito.java"} -->Optional Answer to be used with Mockito#mock(Class, Answer).
        Example that shows how deep stub works:
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, RETURNS_DEEP_STUBS);
        // note that we're stubbing a chain of methods here: getBar().getName()
        when(mock.getBar().getName()).thenReturn("deep");
        // note that we're chaining method calls: getBar().getName()
        assertEquals("deep", mock.getBar().getName());
        WARNING:
        This feature should rarely be required for regular clean code! Leave it for legacy code.
        Mocking a mock to return a mock, to return a mock, (...), to return something meaningful
        hints at violation of Law of Demeter or mocking a value object (a well known anti-pattern).
        Good quote I've seen one day on the web: every time a mock returns a mock a fairy dies.
        Please note that this answer will return existing mocks that matches the stub. This
        behavior is ok with deep stubs and allows verification to work on the last mock of the chain.
        <pre class="code"><code class="java">
        when(mock.getBar(anyString()).getThingy().getName()).thenReturn("deep");
        mock.getBar("candy bar").getThingy().getName();
        assertSame(mock.getBar(anyString()).getThingy().getName(), mock.getBar(anyString()).getThingy().getName());
        verify(mock.getBar("candy bar").getThingy()).getName();
        verify(mock.getBar(anyString()).getThingy()).getName();
        Verification only works with the last mock in the chain. You can use verification modes.
        <pre class="code"><code class="java">
        when(person.getAddress(anyString()).getStreet().getName()).thenReturn("deep");
        when(person.getAddress(anyString()).getStreet(Locale.ITALIAN).getName()).thenReturn("deep");
        when(person.getAddress(anyString()).getStreet(Locale.CHINESE).getName()).thenReturn("deep");
        person.getAddress("the docks").getStreet().getName();
        person.getAddress("the docks").getStreet().getLongName();
        person.getAddress("the docks").getStreet(Locale.ITALIAN).getName();
        person.getAddress("the docks").getStreet(Locale.CHINESE).getName();
        // note that we are actually referring to the very last mock in the stubbing chain.
        InOrder inOrder = inOrder(
        person.getAddress("the docks").getStreet(),
        person.getAddress("the docks").getStreet(Locale.CHINESE),
        person.getAddress("the docks").getStreet(Locale.ITALIAN)
        );
        inOrder.verify(person.getAddress("the docks").getStreet(), times(1)).getName();
        inOrder.verify(person.getAddress("the docks").getStreet()).getLongName();
        inOrder.verify(person.getAddress("the docks").getStreet(Locale.ITALIAN), atLeast(1)).getName();
        inOrder.verify(person.getAddress("the docks").getStreet(Locale.CHINESE)).getName();
        How deep stub work internally?
        <pre class="code"><code class="java">
        //this:
        Foo mock = mock(Foo.class, RETURNS_DEEP_STUBS);
        when(mock.getBar().getName(), "deep");
        //is equivalent of
        Foo foo = mock(Foo.class);
        Bar bar = mock(Bar.class);
        when(foo.getBar()).thenReturn(bar);
        when(bar.getName()).thenReturn("deep");
        This feature will not work when any return type of methods included in the chain cannot be mocked
        (for example: is a primitive or a final class). This is because of java type system.

# File: `ForwardsInvocations.java`

## Class: `ForwardsInvocations`

        <!-- META {"entityType": "Class", "entitySignature": "ForwardsInvocations", "entityFile": "ForwardsInvocations.java"} -->Internal answer to forward invocations on a real instance.
        @since 1.9.5

# File: `StackTraceCleanerProvider.java`

## Method: `StackTraceCleaner getStackTraceCleaner(StackTraceCleaner defaultCleaner)`

        <!-- META {"entityType": "Method", "entitySignature": "StackTraceCleaner getStackTraceCleaner(StackTraceCleaner defaultCleaner)", "entityFile": "StackTraceCleanerProvider.java"} -->Allows configuring custom StackTraceCleaner.
        @param defaultCleaner - Mockito's default StackTraceCleaner
        @return StackTraceCleaner to use

## Interface: `StackTraceCleanerProvider`

        <!-- META {"entityType": "Interface", "entitySignature": "StackTraceCleanerProvider", "entityFile": "StackTraceCleanerProvider.java"} -->An extension point to register custom StackTraceCleaner.
        You can replace Mockito's default StackTraceCleaner.
        You can also 'enhance' Mockito's default behavior
        because the default cleaner is passed as parameter to the method.
        Registering custom StackTraceCleaner is done in similar manner as the MockMaker implementation.
        See the default implementation: org.mockito.internal.exceptions.stacktrace.DefaultStackTraceCleanerProvider

# File: `ArrayIterator.java`

## Class: `ArrayIterator`

        <!-- META {"entityType": "Class", "entitySignature": "ArrayIterator", "entityFile": "ArrayIterator.java"} -->Inspired on hamcrest, internal package class,
        TODO add specific unit tests instead of relying on higher level unit tests

# File: `EqualsBuilder.java`

## Method: `public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients, Class reflectUpToClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients, Class reflectUpToClass)", "entityFile": "EqualsBuilder.java"} --><!-- 29f444ee-1782-11ea-a04a-333445793454 <=< ACCEPT -->This method uses reflection to determine if the two Objects
        are equal.
        It uses AccessibleObject.setAccessible to gain access to private
        fields. This means that it will throw a security exception if run under
        a security manager, if the permissions are not set up correctly. It is also
        not as efficient as testing explicitly.
        If the testTransients parameter is set to true, transient
        members will be tested, otherwise they are ignored, as they are likely
        derived fields, and not part of the value of the Object.
        Static fields will not be included. Superclass fields will be appended
        up to and including the specified superclass. A null superclass is treated
        as java.lang.Object.
        @param lhs  this object
        @param rhs  the other object
        @param testTransients  whether to include transient fields
        @param reflectUpToClass  the superclass to reflect up to (inclusive),
        may be null
        @return true if the two Objects have tested equals.
        @since 2.0<!-- ACCEPT >=> 29f444ee-1782-11ea-a04a-333445793454 -->

# File: `FormattedText.java`

## Class: `FormattedText`

        <!-- META {"entityType": "Class", "entitySignature": "FormattedText", "entityFile": "FormattedText.java"} -->Contains text that has already been formatted
        and hence it does not need any formatting (like quotes around string, etc.)

# File: `Mockito.java`

## Field: `CALLS_REAL_METHODS`

        <!-- META {"entityType": "Field", "entitySignature": "CALLS_REAL_METHODS", "entityFile": "Mockito.java"} --><!-- 305f42d4-1781-11ea-8400-333445793454 <=< ACCEPT -->Optional Answer to be used with Mockito#mock(Class, Answer)
        Answer can be used to define the return values of unstubbed invocations.
        This implementation can be helpful when working with legacy code.
        When this implementation is used, unstubbed methods will delegate to the real implementation.
        This is a way to create a partial mock object that calls real methods by default.
        As usual you are going to read the partial mock warning:
        Object oriented programming is more less tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        Example:
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, CALLS_REAL_METHODS);
        // this calls the real implementation of Foo.getSomething()
        value = mock.getSomething();
        when(mock.getSomething()).thenReturn(fakeValue);
        // now fakeValue is returned
        value = mock.getSomething();
        <!-- ACCEPT >=> 305f42d4-1781-11ea-8400-333445793454 -->

# File: `ConsoleSpammingMockitoJUnitRunner.java`

## Class: `ConsoleSpammingMockitoJUnitRunner`

        <!-- META {"entityType": "Class", "entitySignature": "ConsoleSpammingMockitoJUnitRunner", "entityFile": "ConsoleSpammingMockitoJUnitRunner.java"} -->Uses JUnit 4.5 runner BlockJUnit4ClassRunner.
        Experimental implementation that suppose to improve tdd/testing experience.
        Don't hesitate to send feedback to mockito@googlegroups.com
        It is very likely it will change in the next version!
        This runner does exactly what MockitoJUnitRunner does but also
        prints warnings that might be useful.
        The point is that Mockito should help the tdd developer to quickly figure out if the test fails for the right reason.
        Then the developer can implement the functionality.
        Also when the test fails it should be easy to figure out why the test fails.
        Sometimes when the test fails, the underlying reason is that stubbed method was called with wrong arguments.
        Sometimes it fails because one forgets to stub a method or forgets to call a stubbed method.
        All above problems are not immediately obvious.
        One way of approaching this problem is full-blown 'expect' API.
        However it means the 'expectations upfront' business which is not in line with core Mockito concepts.
        After all, the essence of testing are explicit assertions that are described consistently at the bottom of the test method.
        Here's the experiment: a warning is printed to the standard output if the test fails.
        Also, you get a clickabe link to the line of code. You can immediately jump to the place in code where the potential problem is.
        Let's say your test fails on assertion.
        Let's say the underlying reason is a stubbed method that was called with different arguments:
        <pre class="code"><code class="java">
        //test:
        Dictionary dictionary = new Dictionary(translator);
        when(translator.translate("Mockito")).thenReturn("cool framework");
        String translated = dictionary.search("Mockito");
        assertEquals("cool framework", translated);
        //code:
        public String search(String word) {
        ...
        return translator.translate("oups");
        On standard output you'll see something like that:
        <pre class="code"><code class="java">
        [Mockito] Warning - stubbed method called with different arguments.
        Stubbed this way:
        translator.translate("Mockito");
        org.dictionary.SmartDictionaryTest.shouldFindTranslation(SmartDictionaryTest.java:27)
        But called with different arguments:
        translator.translate("oups");
        org.dictionary.SmartDictionary.search(SmartDictionary.java:15)
        Note that it is just a warning, not an assertion.
        The test fails on assertion because it's the assertion's duty to document what the test stands for and what behavior it proves.
        Warnings just makes it quicker to figure out if the test fails for the right reason.
        Note that code links printed to the console are clickable in any decent IDE (e.g. Eclipse).
        So far I identified 2 cases when warnings are printed:
        unsued stub
        stubbed method but called with different arguments
        Do you think it is useful or not? Drop us an email at mockito@googlegroups.com

# File: `MatcherToString.java`

## Method: `static String toString(ArgumentMatcher matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "static String toString(ArgumentMatcher matcher)", "entityFile": "MatcherToString.java"} -->Attempts to provide more descriptive toString() for given matcher.
        Searches matcher class hierarchy for toString() method. If it is found it will be used.
        If no toString() is defined for the matcher hierarchy,
        uses decamelized class name instead of default Object.toString().
        This way we can promote meaningful names for custom matchers.
        @param matcher
        @return

# File: `EqualsBuilder.java`

## Method: `public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients, Class reflectUpToClass, String[] excludeFields)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean reflectionEquals(Object lhs, Object rhs, boolean testTransients, Class reflectUpToClass, String[] excludeFields)", "entityFile": "EqualsBuilder.java"} --><!-- 29f444ee-1782-11ea-a04a-333445793454 <=< ACCEPT -->This method uses reflection to determine if the two Objects
        are equal.
        It uses AccessibleObject.setAccessible to gain access to private
        fields. This means that it will throw a security exception if run under
        a security manager, if the permissions are not set up correctly. It is also
        not as efficient as testing explicitly.
        If the testTransients parameter is set to true, transient
        members will be tested, otherwise they are ignored, as they are likely
        derived fields, and not part of the value of the Object.
        Static fields will not be included. Superclass fields will be appended
        up to and including the specified superclass. A null superclass is treated
        as java.lang.Object.
        @param lhs  this object
        @param rhs  the other object
        @param testTransients  whether to include transient fields
        @param reflectUpToClass  the superclass to reflect up to (inclusive),
        may be null
        @param excludeFields  array of field names to exclude from testing
        @return true if the two Objects have tested equals.
        @since 2.0
        <!-- ACCEPT >=> 29f444ee-1782-11ea-a04a-333445793454 -->

# File: `MatcherToString.java`

## Class: `MatcherToString`

        <!-- META {"entityType": "Class", "entitySignature": "MatcherToString", "entityFile": "MatcherToString.java"} -->Provides better toString() text for matcher that don't have toString() method declared.

# File: `Mockito.java`

## Field: `RETURNS_SELF`

        <!-- META {"entityType": "Field", "entitySignature": "RETURNS_SELF", "entityFile": "Mockito.java"} -->Optional Answer to be used with Mockito#mock(Class, Answer).
        Allows Builder mocks to return itself whenever a method is invoked that returns a Type equal
        to the class or a superclass.
        Keep in mind this answer uses the return type of a method.
        If this type is assignable to the class of the mock, it will return the mock.
        Therefore if you have a method returning a superclass (for example Object) it will match and return the mock.
        Consider a HttpBuilder used in a HttpRequesterWithHeaders.
        <pre class="code"><code class="java">
        public class HttpRequesterWithHeaders {
        private HttpBuilder builder;
        public HttpRequesterWithHeaders(HttpBuilder builder) {
        this.builder = builder;
        }
        public String request(String uri) {
        return builder.withUrl(uri)
        .withHeader("Content-type: application/json")
        .withHeader("Authorization: Bearer")
        .request();
        }
        }
        private static class HttpBuilder {
        private String uri;
        private List&lt;String&gt; headers;
        public HttpBuilder() {
        this.headers = new ArrayList&lt;String&gt;();
        }
        public HttpBuilder withUrl(String uri) {
        this.uri = uri;
        return this;
        }
        public HttpBuilder withHeader(String header) {
        this.headers.add(header);
        return this;
        }
        public String request() {
        return uri + headers.toString();
        }
        }
        The following test will succeed
        @Test
        public void use_full_builder_with_terminating_method() {
        HttpBuilder builder = mock(HttpBuilder.class, RETURNS_SELF);
        HttpRequesterWithHeaders requester = new HttpRequesterWithHeaders(builder);
        String response = "StatusCode: 200";
        when(builder.request()).thenReturn(response);
        assertThat(requester.request("URI")).isEqualTo(response);
        }

# File: `MockitoJUnit44Runner.java`

## Class: `MockitoJUnit44Runner`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoJUnit44Runner", "entityFile": "MockitoJUnit44Runner.java"} -->Deprecated: Simply use MockitoJUnitRunner
        Compatible only with JUnit 4.4, this runner adds following behavior:
        Initializes mocks annotated with Mock,
        so that explicit usage of MockitoAnnotations#initMocks(Object) is not necessary.
        Mocks are initialized before each test method.
        validates framework usage after each test method. See javadoc for Mockito#validateMockitoUsage().
        Runner is completely optional - there are other ways you can get @Mock working, for example by writing a base class.
        Explicitly validating framework usage is also optional because it is triggered automatically by Mockito every time you use the framework.
        See javadoc for Mockito#validateMockitoUsage().
        Read more about @Mock annotation in javadoc for MockitoAnnotations
        Example:
        <pre class="code"><code class="java">
        @RunWith(MockitoJUnitRunner.class)
        public class ExampleTest {
        @Mock
        private List list;
        @Test
        public void shouldDoSomething() {
        list.add(100);
        }
        }

# File: `EqualsBuilder.java`

## Method: `private static void reflectionAppend(Object lhs, Object rhs, Class clazz, EqualsBuilder builder, boolean useTransients, String[] excludeFields)`

        <!-- META {"entityType": "Method", "entitySignature": "private static void reflectionAppend(Object lhs, Object rhs, Class clazz, EqualsBuilder builder, boolean useTransients, String[] excludeFields)", "entityFile": "EqualsBuilder.java"} -->Appends the fields and values defined by the given object of the
        given Class.
        @param lhs  the left hand object
        @param rhs  the right hand object
        @param clazz  the class to append details of
        @param builder  the builder to append to
        @param useTransients  whether to test transient fields
        @param excludeFields  array of field names to exclude from testing

# File: `Mockito.java`

## Method: `public static T mock(Class<T> classToMock)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T mock(Class<T> classToMock)", "entityFile": "Mockito.java"} -->Creates mock object of given class or interface.
        See examples in javadoc for Mockito class
        @param classToMock class or interface to mock
        @return mock object

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder appendSuper(boolean superEquals)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder appendSuper(boolean superEquals)", "entityFile": "EqualsBuilder.java"} -->Adds the result of super.equals() to this builder.
        @param superEquals  the result of calling super.equals()
        @return EqualsBuilder - used to chain calls.
        @since 2.0

## Method: `public EqualsBuilder append(Object lhs, Object rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(Object lhs, Object rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two Objects are equal using their
        equals method.
        @param lhs  the left hand object
        @param rhs  the right hand object
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `MockitoJUnitRunner.java`

## Class: `MockitoJUnitRunner`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoJUnitRunner", "entityFile": "MockitoJUnitRunner.java"} -->Compatible with JUnit 4.4 and higher, this runner adds following behavior:
        Initializes mocks annotated with Mock,
        so that explicit usage of MockitoAnnotations#initMocks(Object) is not necessary.
        Mocks are initialized before each test method.
        validates framework usage after each test method. See javadoc for Mockito#validateMockitoUsage().
        Runner is completely optional - there are other ways you can get @Mock working, for example by writing a base class.
        Explicitly validating framework usage is also optional because it is triggered automatically by Mockito every time you use the framework.
        See javadoc for Mockito#validateMockitoUsage().
        Read more about @Mock annotation in javadoc for MockitoAnnotations
        <pre class="code"><code class="java">
        @RunWith(MockitoJUnitRunner.class)
        public class ExampleTest {
        @Mock
        private List list;
        @Test
        public void shouldDoSomething() {
        list.add(100);
        }
        }

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(long lhs, long rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(long lhs, long rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two long s are equal.
        @param lhs
        the left hand long
        @param rhs
        the right hand long
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

## Method: `public EqualsBuilder append(int lhs, int rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(int lhs, int rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two ints are equal.
        @param lhs  the left hand int
        @param rhs  the right hand int
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `ValuePrinter.java`

## Method: `public static String print(Object value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String print(Object value)", "entityFile": "ValuePrinter.java"} -->Prints given value so that it is neatly readable by humans.
        Handles explosive toString() implementations.

# File: `Mockito.java`

## Method: `public static T mock(Class<T> classToMock, String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T mock(Class<T> classToMock, String name)", "entityFile": "Mockito.java"} -->Specifies mock name. Naming mocks can be helpful for debugging - the name is used in all verification errors.
        Beware that naming mocks is not a solution for complex code which uses too many mocks or collaborators.
        If you have too many mocks then refactor the code so that it's easy to test/debug without necessity of naming mocks.
        If you use @Mock annotation then you've got naming mocks for free! @Mock uses field name as mock name. Mock Read more.
        See examples in javadoc for Mockito class
        @param classToMock class or interface to mock
        @param name of the mock
        @return mock object

# File: `ValuePrinter.java`

## Method: `public static String printValues(String start, String separator, String end, Iterator values)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String printValues(String start, String separator, String end, Iterator values)", "entityFile": "ValuePrinter.java"} -->Print values in a nice format, e.g. (1, 2, 3)
        @param start the beginning of the values, e.g. "("
        @param separator the separator of values, e.g. ", "
        @param end the end of the values, e.g. ")"
        @param values the values to print
        @return neatly formatted value list

## Class: `ValuePrinter`

        <!-- META {"entityType": "Class", "entitySignature": "ValuePrinter", "entityFile": "ValuePrinter.java"} -->Prints a Java object value in a way humans can read it neatly.
        Inspired on hamcrest. Used for printing arguments in verification errors.

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(short lhs, short rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(short lhs, short rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two shorts are equal.
        @param lhs  the left hand short
        @param rhs  the right hand short
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `Mockito.java`

## Method: `public static MockingDetails mockingDetails(Object toInspect)`

        <!-- META {"entityType": "Method", "entitySignature": "public static MockingDetails mockingDetails(Object toInspect)", "entityFile": "Mockito.java"} -->Returns a MockingDetails instance that enables inspecting a particular object for Mockito related information.
        Can be used to find out if given object is a Mockito mock
        or to find out if a given mock is a spy or mock.
        In future Mockito versions MockingDetails may grow and provide other useful information about the mock,
        e.g. invocations, stubbing info, etc.
        @param toInspect - object to inspect. null input is allowed.
        @return A org.mockito.MockingDetails instance.
        @since 1.9.5

# File: `VerboseMockitoJUnitRunner.java`

## Class: `VerboseMockitoJUnitRunner`

        <!-- META {"entityType": "Class", "entitySignature": "VerboseMockitoJUnitRunner", "entityFile": "VerboseMockitoJUnitRunner.java"} -->Experimental implementation that suppose to improve tdd/testing experience.
        Don't hesitate to send feedback to mockito@googlegroups.com
        It is very likely it will change in the next version!
        This runner does exactly what MockitoJUnitRunner does but also
        adds extra Mocktio hints to the exception message.
        The point is that Mockito should help the tdd developer to quickly figure out if the test fails for the right reason and track the reason.
        The implementation is pretty hacky - it uses brute force of reflection to modify the exception message and add extra mockito hints.
        You've been warned.
        Do you think it is useful or not? Drop us an email at mockito@googlegroups.com
        Experimental implementation - will change in future!

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(char lhs, char rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(char lhs, char rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two chars are equal.
        @param lhs  the left hand char
        @param rhs  the right hand char
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `VarargMatcher.java`

## Interface: `VarargMatcher`

        <!-- META {"entityType": "Interface", "entitySignature": "VarargMatcher", "entityFile": "VarargMatcher.java"} -->Internal interface that informs Mockito that the matcher is intended to capture varargs.
        This information is needed when mockito collects the arguments.

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(byte lhs, byte rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(byte lhs, byte rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two bytes are equal.
        @param lhs  the left hand byte
        @param rhs  the right hand byte
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `Mockito.java`

## Method: `public static T mock(Class<T> classToMock, Answer defaultAnswer)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T mock(Class<T> classToMock, Answer defaultAnswer)", "entityFile": "Mockito.java"} --><!-- 90596ef4-1782-11ea-8ba9-333445793454 <=< ACCEPT -->Creates mock with a specified strategy for its answers to interactions.
        It's quite an advanced feature and typically you don't need it to write decent tests.
        However it can be helpful when working with legacy systems.
        It is the default answer so it will be used only when you don't stub the method call.
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, RETURNS_SMART_NULLS);
        Foo mockTwo = mock(Foo.class, new YourOwnAnswer());
        See examples in javadoc for Mockito class
        @param classToMock class or interface to mock
        @param defaultAnswer default answer for unstubbed methods
        @return mock object<!-- ACCEPT >=> 90596ef4-1782-11ea-8ba9-333445793454 -->

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(double lhs, double rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(double lhs, double rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1784-11ea-b73a-333445793454 <=< ACCEPT -->Test if two doubles are equal by testing that the
        pattern of bits returned by doubleToLong are equal.
        This handles NaNs, Infinities, and -0.0.
        It is compatible with the hash code generated by
        HashCodeBuilder.
        @param lhs  the left hand double
        @param rhs  the right hand double
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1784-11ea-b73a-333445793454 -->

## Method: `public EqualsBuilder append(float lhs, float rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(float lhs, float rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1784-11ea-b73a-333445793454 <=< ACCEPT -->Test if two floats are equal byt testing that the
        pattern of bits returned by doubleToLong are equal.
        This handles NaNs, Infinities, and -0.0.
        It is compatible with the hash code generated by
        HashCodeBuilder.
        @param lhs  the left hand float
        @param rhs  the right hand float
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1784-11ea-b73a-333445793454 -->

## Method: `public EqualsBuilder append(boolean lhs, boolean rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(boolean lhs, boolean rhs)", "entityFile": "EqualsBuilder.java"} --><!-- a233bbc6-1783-11ea-b73a-333445793454 <=< ACCEPT -->Test if two booleanss are equal.
        @param lhs  the left hand boolean
        @param rhs  the right hand boolean
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> a233bbc6-1783-11ea-b73a-333445793454 -->

# File: `Mockito.java`

## Method: `public static T mock(Class<T> classToMock, MockSettings mockSettings)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T mock(Class<T> classToMock, MockSettings mockSettings)", "entityFile": "Mockito.java"} -->Creates a mock with some non-standard settings.
        The number of configuration points for a mock grows
        so we need a fluent way to introduce new configuration without adding more and more overloaded Mockito.mock() methods.
        Hence MockSettings.
        <pre class="code"><code class="java">
        Listener mock = mock(Listener.class, withSettings()
        .name("firstListner").defaultBehavior(RETURNS_SMART_NULLS));
        );
        Use it carefully and occasionally. What might be reason your test needs non-standard mocks?
        Is the code under test so complicated that it requires non-standard mocks?
        Wouldn't you prefer to refactor the code under test so it is testable in a simple way?
        See also Mockito#withSettings()
        See examples in javadoc for Mockito class
        @param classToMock class or interface to mock
        @param mockSettings additional mock settings
        @return mock object

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(Object[] lhs, Object[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(Object[] lhs, Object[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Performs a deep comparison of two Object arrays.
        This also will be called for the top level of
        multi-dimensional, ragged, and multi-typed arrays.
        @param lhs  the left hand Object[]
        @param rhs  the right hand Object[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

## Method: `public EqualsBuilder append(long[] lhs, long[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(long[] lhs, long[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of long. Length and all
        values are compared.
        The method #append(long, long) is used.
        @param lhs  the left hand long[]
        @param rhs  the right hand long[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

# File: `Spy.java`

## Annotation: `Spy`

        <!-- META {"entityType": "Annotation", "entitySignature": "Spy", "entityFile": "Spy.java"} -->Allows shorthand wrapping of field instances in an spy object.
        Example:
        <pre class="code"><code class="java">
        public class Test{
        //Instance for spying is created by calling constructor explicitly:
        &#64;Spy Foo spyOnFoo = new Foo("argument");
        //Instance for spying is created by mockito via reflection (only default constructors supported):
        &#64;Spy Bar spyOnBar;
        &#64;Before
        public void init(){
        MockitoAnnotations.initMocks(this);
        }
        ...
        }
        Same as doing:
        <pre class="code"><code class="java">
        Foo spyOnFoo = Mockito.spy(new Foo("argument"));
        Bar spyOnFoo = Mockito.spy(new Bar());
        The field annotated with @Spy can be initialized by Mockito if a zero argument constructor
        can be found in the type (even private). But Mockito cannot instantiate inner classes, local classes,
        abstract classes and interfaces.
        The field annotated with @Spy can be initialized explicitly at declaration point.
        Alternatively, if you don't provide the instance Mockito will try to find zero argument constructor (even private)
        and create an instance for you.
        But Mockito cannot instantiate inner classes, local classes, abstract classes and interfaces.
        For example this class can be instantiated by Mockito :
        <pre class="code"><code class="java">public class Bar {
        private Bar() {}
        public Bar(String publicConstructorWithOneArg) {}
        }
        Important gotcha on spying real objects!
        Sometimes it's impossible or impractical to use Mockito#when(Object) for stubbing spies.
        Therefore for spies it is recommended to always use doReturn|Answer|Throw()|CallRealMethod
        family of methods for stubbing. Example:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing
        doReturn("foo").when(spy).get(0);
        Mockito *does not* delegate calls to the passed real instance, instead it actually creates a copy of it.
        So if you keep the real instance and interact with it, don't expect the spied to be aware of those interaction
        and their effect on real instance state.
        The corollary is that when an *unstubbed* method is called *on the spy* but *not on the real instance*,
        you won't see any effects on the real instance.
        Watch out for final methods.
        Mockito doesn't mock final methods so the bottom line is: when you spy on real objects + you try to stub a final method = trouble.
        Also you won't be able to verify those method as well.
        One last warning : if you call MockitoAnnotations.initMocks(this) in a
        super class constructor then this will not work. It is because fields
        in subclass are only instantiated after super class constructor has returned.
        It's better to use &#64;Before.
        Instead you can also put initMocks() in your JUnit runner (@RunWith) or use the built-in
        org.mockito.runners.MockitoJUnitRunner.
        Note that the spy won't have any annotations of the spied type, because CGLIB won't rewrite them.
        It may troublesome for code that rely on the spy to have these annotations.
        @see Mockito#spy(Object)
        @see Mock
        @see InjectMocks
        @see MockitoAnnotations#initMocks(Object)
        @see org.mockito.runners.MockitoJUnitRunner
        @since 1.8.3

# File: `Answer.java`

## Method: `T answer(InvocationOnMock invocation) throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "T answer(InvocationOnMock invocation) throws Throwable", "entityFile": "Answer.java"} -->@param invocation the invocation on the mock.
        @return the value to be returned
        @throws Throwable the throwable to be thrown

# File: `MockitoCore.java`

## Method: `public Invocation getLastInvocation()`

        <!-- META {"entityType": "Method", "entitySignature": "public Invocation getLastInvocation()", "entityFile": "MockitoCore.java"} -->For testing purposes only. Is not the part of main API.
        @return last invocation

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(int[] lhs, int[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(int[] lhs, int[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of int. Length and all
        values are compared.
        The method #append(int, int) is used.
        @param lhs  the left hand int[]
        @param rhs  the right hand int[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

# File: `Answer.java`

## Interface: `Answer`

        <!-- META {"entityType": "Interface", "entitySignature": "Answer", "entityFile": "Answer.java"} -->Generic interface to be used for configuring mock's answer.
        Answer specifies an action that is executed and a return value that is returned when you interact with the mock.
        Example of stubbing a mock with custom answer:
        <pre class="code"><code class="java">
        when(mock.someMethod(anyString())).thenAnswer(new Answer() {
        Object answer(InvocationOnMock invocation) {
        Object[] args = invocation.getArguments();
        Object mock = invocation.getMock();
        return "called with arguments: " + Arrays.toString(args);
        }
        });
        //Following prints "called with arguments: [foo]"
        System.out.println(mock.someMethod("foo"));
        @param <T> the type to return.

# File: `Mockito.java`

## Method: `public static T spy(T object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T spy(T object)", "entityFile": "Mockito.java"} -->Creates a spy of the real object. The spy calls real methods unless they are stubbed.
        Real spies should be used carefully and occasionally, for example when dealing with legacy code.
        As usual you are going to read the partial mock warning:
        Object oriented programming tackles complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        Example:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //optionally, you can stub out some methods:
        when(spy.size()).thenReturn(100);
        //using the spy calls real methods
        spy.add("one");
        spy.add("two");
        //prints "one" - the first element of a list
        System.out.println(spy.get(0));
        //size() method was stubbed - 100 is printed
        System.out.println(spy.size());
        //optionally, you can verify
        verify(spy).add("one");
        verify(spy).add("two");
        Important gotcha on spying real objects!
        Sometimes it's impossible or impractical to use Mockito#when(Object) for stubbing spies.
        Therefore for spies it is recommended to always use doReturn|Answer|Throw()|CallRealMethod
        family of methods for stubbing. Example:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing
        doReturn("foo").when(spy).get(0);
        Mockito *does not* delegate calls to the passed real instance, instead it actually creates a copy of it.
        So if you keep the real instance and interact with it, don't expect the spied to be aware of those interaction
        and their effect on real instance state.
        The corollary is that when an *unstubbed* method is called *on the spy* but *not on the real instance*,
        you won't see any effects on the real instance.
        Watch out for final methods.
        Mockito doesn't mock final methods so the bottom line is: when you spy on real objects + you try to stub a final method = trouble.
        Also you won't be able to verify those method as well.
        See examples in javadoc for Mockito class
        Note that the spy won't have any annotations of the spied type, because CGLIB won't rewrite them.
        It may troublesome for code that rely on the spy to have these annotations.
        @param object
        to spy on
        @return a spy of the real object

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(short[] lhs, short[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(short[] lhs, short[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of short. Length and all
        values are compared.
        The method #append(short, short) is used.
        @param lhs  the left hand short[]
        @param rhs  the right hand short[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

# File: `ReturnsElementsOf.java`

## Class: `ReturnsElementsOf`

        <!-- META {"entityType": "Class", "entitySignature": "ReturnsElementsOf", "entityFile": "ReturnsElementsOf.java"} --><!-- 62e3dc36-1785-11ea-bbed-333445793454 <=< ACCEPT -->Returns elements of the collection. Keeps returning the last element forever.
        Might be useful on occasion when you have a collection of elements to return.
        <pre class="code"><code class="java">
        //this:
        when(mock.foo()).thenReturn(1, 2, 3);
        //is equivalent to:
        when(mock.foo()).thenReturn(new ReturnsElementsOf(Arrays.asList(1, 2, 3)));
        @deprecated Use org.mockito.AdditionalAnswers#returnsElementsOf<!-- ACCEPT >=> 62e3dc36-1785-11ea-bbed-333445793454 -->

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(char[] lhs, char[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(char[] lhs, char[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of char. Length and all
        values are compared.
        The method #append(char, char) is used.
        @param lhs  the left hand char[]
        @param rhs  the right hand char[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

## Method: `public EqualsBuilder append(byte[] lhs, byte[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(byte[] lhs, byte[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of byte. Length and all
        values are compared.
        The method #append(byte, byte) is used.
        @param lhs  the left hand byte[]
        @param rhs  the right hand byte[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

## Method: `public EqualsBuilder append(double[] lhs, double[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(double[] lhs, double[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of double. Length and all
        values are compared.
        The method #append(double, double) is used.
        @param lhs  the left hand double[]
        @param rhs  the right hand double[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

## Method: `public EqualsBuilder append(float[] lhs, float[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(float[] lhs, float[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of float. Length and all
        values are compared.
        The method #append(float, float) is used.
        @param lhs  the left hand float[]
        @param rhs  the right hand float[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

# File: `Mockito.java`

## Method: `public static T spy(Class<T> classToSpy)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T spy(Class<T> classToSpy)", "entityFile": "Mockito.java"} -->Please refer to the documentation of #spy(Object).
        Overusing spies hints at code design smells.
        This method, in contrast to the original #spy(Object), creates a spy based on class instead of an object.
        Sometimes it is more convenient to create spy based on the class and avoid providing an instance of a spied object.
        This is particularly useful for spying on abstract classes because they cannot be instantiated.
        See also MockSettings#useConstructor().
        Examples:
        <pre class="code"><code class="java">
        SomeAbstract spy = spy(SomeAbstract.class);
        //Robust API, via settings builder:
        OtherAbstract spy = mock(OtherAbstract.class, withSettings()
        .useConstructor().defaultAnswer(CALLS_REAL_METHODS));
        //Mocking a non-static inner abstract class:
        InnerAbstract spy = mock(InnerAbstract.class, withSettings()
        .useConstructor().outerInstance(outerInstance).defaultAnswer(CALLS_REAL_METHODS));
        @param classToSpy the class to spy
        @param <T> type of the spy
        @return a spy of the provided class
        @since 1.10.12

# File: `EqualsBuilder.java`

## Method: `public EqualsBuilder append(boolean[] lhs, boolean[] rhs)`

        <!-- META {"entityType": "Method", "entitySignature": "public EqualsBuilder append(boolean[] lhs, boolean[] rhs)", "entityFile": "EqualsBuilder.java"} --><!-- 0ccb24ba-1783-11ea-a462-333445793454 <=< ACCEPT -->Deep comparison of array of boolean. Length and all
        values are compared.
        The method #append(boolean, boolean) is used.
        @param lhs  the left hand boolean[]
        @param rhs  the right hand boolean[]
        @return EqualsBuilder - used to chain calls.<!-- ACCEPT >=> 0ccb24ba-1783-11ea-a462-333445793454 -->

# File: `DeprecatedOngoingStubbing.java`

## Method: `DeprecatedOngoingStubbing<T> toReturn(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "DeprecatedOngoingStubbing<T> toReturn(T value)", "entityFile": "DeprecatedOngoingStubbing.java"} -->Set a return value for the stubbed method. E.g:
        <pre class="code"><code class="java">
        stub(mock.someMethod()).toReturn(10);
        See examples in javadoc for Mockito#stub
        @param value return value
        @return iOngoingStubbing object that allows stubbing consecutive calls

# File: `EqualsBuilder.java`

## Method: `public boolean isEquals()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isEquals()", "entityFile": "EqualsBuilder.java"} -->Returns true if the fields that have been checked
        are all equal.
        @return boolean

## Method: `protected void setEquals(boolean isEquals)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void setEquals(boolean isEquals)", "entityFile": "EqualsBuilder.java"} -->Sets the isEquals value.
        @param isEquals The value to set.
        @since 2.1

# File: `DeprecatedOngoingStubbing.java`

## Method: `DeprecatedOngoingStubbing<T> toThrow(Throwable throwable)`

        <!-- META {"entityType": "Method", "entitySignature": "DeprecatedOngoingStubbing<T> toThrow(Throwable throwable)", "entityFile": "DeprecatedOngoingStubbing.java"} -->Set a Throwable to be thrown when the stubbed method is called. E.g:
        <pre class="code"><code class="java">
        stub(mock.someMethod()).toThrow(new RuntimeException());
        If throwable is a checked exception then it has to
        match one of the checked exceptions of method signature.
        See examples in javadoc for Mockito#stub
        @param throwable to be thrown on method invocation
        @return iOngoingStubbing object that allows stubbing consecutive calls

# File: `Mockito.java`

## Method: `public static DeprecatedOngoingStubbing<T> stub(T methodCall)`

        <!-- META {"entityType": "Method", "entitySignature": "public static DeprecatedOngoingStubbing<T> stub(T methodCall)", "entityFile": "Mockito.java"} -->Stubs a method call with return value or an exception. E.g:
        <pre class="code"><code class="java">
        stub(mock.someMethod()).toReturn(10);
        //you can use flexible argument matchers, e.g:
        stub(mock.someMethod(anyString())).toReturn(10);
        //setting exception to be thrown:
        stub(mock.someMethod("some arg")).toThrow(new RuntimeException());
        //you can stub with different behavior for consecutive method calls.
        //Last stubbing (e.g: toReturn("foo")) determines the behavior for further consecutive calls.
        stub(mock.someMethod("some arg"))
        .toThrow(new RuntimeException())
        .toReturn("foo");
        Some users find stub() confusing therefore Mockito#when(Object) is recommended over stub()
        <pre class="code"><code class="java">
        //Instead of:
        stub(mock.count()).toReturn(10);
        //You can do:
        when(mock.count()).thenReturn(10);
        For stubbing void methods with throwables see: Mockito#doThrow(Throwable...)
        Stubbing can be overridden: for example common stubbing can go to fixture
        setup but the test methods can override it.
        Please note that overridding stubbing is a potential code smell that points out too much stubbing.
        Once stubbed, the method will always return stubbed value regardless
        of how many times it is called.
        Last stubbing is more important - when you stubbed the same method with
        the same arguments many times.
        Although it is possible to verify a stubbed invocation, usually it's just redundant.
        Let's say you've stubbed foo.bar().
        If your code cares what foo.bar() returns then something else breaks(often before even verify() gets executed).
        If your code doesn't care what get(0) returns then it should not be stubbed.
        Not convinced? See <a href="http://monkeyisland.pl/2008/04/26/asking-and-telling">here.
        @param methodCall
        method call
        @return DeprecatedOngoingStubbing object to set stubbed value/exception

# File: `DeprecatedOngoingStubbing.java`

## Method: `DeprecatedOngoingStubbing<T> toAnswer(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "DeprecatedOngoingStubbing<T> toAnswer(Answer<?> answer)", "entityFile": "DeprecatedOngoingStubbing.java"} -->Set a generic Answer for the stubbed method. E.g:
        <pre class="code"><code class="java">
        stub(mock.someMethod(10)).toAnswer(new Answer&lt;Integer&gt;() {
        public Integer answer(InvocationOnMock invocation) throws Throwable {
        return (Integer) invocation.getArguments()[0];
        }
        }
        @param answer the custom answer to execute.
        @return iOngoingStubbing object that allows stubbing consecutive calls

## Interface: `DeprecatedOngoingStubbing`

        <!-- META {"entityType": "Interface", "entitySignature": "DeprecatedOngoingStubbing", "entityFile": "DeprecatedOngoingStubbing.java"} -->Stubs a method call with return value or an exception. E.g:
        <pre class="code"><code class="java">
        stub(mock.someMethod()).toReturn(10);
        //you can use flexible argument matchers, e.g:
        stub(mock.someMethod(anyString())).toReturn(10);
        //setting exception to be thrown:
        stub(mock.someMethod("some arg")).toThrow(new RuntimeException());
        //you can stub with different behavior for consecutive method calls.
        //Last stubbing (e.g: toReturn("foo")) determines the behavior for further consecutive calls.
        stub(mock.someMethod("some arg"))
        .toThrow(new RuntimeException())
        .toReturn("foo");
        See examples in javadoc for Mockito#stub

# File: `EqualsBuilder.java`

## Class: `EqualsBuilder`

        <!-- META {"entityType": "Class", "entitySignature": "EqualsBuilder", "entityFile": "EqualsBuilder.java"} -->Assists in implementing Object#equals(Object) methods.
        This class provides methods to build a good equals method for any
        class. It follows rules laid out in
        <a href="http://java.sun.com/docs/books/effective/index.html">Effective Java
        , by Joshua Bloch. In particular the rule for comparing doubles,
        floats, and arrays can be tricky. Also, making sure that
        equals() and hashCode() are consistent can be
        difficult.
        Two Objects that compare as equals must generate the same hash code,
        but two Objects with the same hash code do not have to be equal.
        All relevant fields should be included in the calculation of equals.
        Derived fields may be ignored. In particular, any field used in
        generating a hash code must be used in the equals method, and vice
        versa.
        Typical use for the code is as follows:
        <pre class="code"><code class="java">
        public boolean equals(Object obj) {
        if (obj == null) { return false; }
        if (obj == this) { return true; }
        if (obj.getClass() != getClass()) {
        return false;
        }
        MyClass rhs = (MyClass) obj;
        return new EqualsBuilder()
        .appendSuper(super.equals(obj))
        .append(field1, rhs.field1)
        .append(field2, rhs.field2)
        .append(field3, rhs.field3)
        .isEquals();
        }
        Alternatively, there is a method that uses reflection to determine
        the fields to test. Because these fields are usually private, the method,
        reflectionEquals, uses AccessibleObject.setAccessible to
        change the visibility of the fields. This will fail under a security
        manager, unless the appropriate permissions are set up correctly. It is
        also slower than testing explicitly.
        A typical invocation for this method would look like:
        <pre class="code"><code class="java">
        public boolean equals(Object obj) {
        return EqualsBuilder.reflectionEquals(this, obj);
        }
        @author <a href="mailto:steve.downey@netfolio.com">Steve Downey
        @author Stephen Colebourne
        @author Gary Gregory
        @author Pete Gieser
        @author Arun Mammen Thomas
        @since 1.0
        @version $Id: EqualsBuilder.java 611543 2008-01-13 07:00:22Z bayard $

# File: `MockingProgress.java`

## Method: `void resetOngoingStubbing()`

        <!-- META {"entityType": "Method", "entitySignature": "void resetOngoingStubbing()", "entityFile": "MockingProgress.java"} -->Removes ongoing stubbing so that in case the framework is misused
        state validation errors are more accurate

# File: `Mockito.java`

## Method: `public static OngoingStubbing<T> when(T methodCall)`

        <!-- META {"entityType": "Method", "entitySignature": "public static OngoingStubbing<T> when(T methodCall)", "entityFile": "Mockito.java"} -->Enables stubbing methods. Use it when you want the mock to return particular value when particular method is called.
        Simply put: "When the x method is called then return y".
        when() is a successor of deprecated Mockito#stub(Object)
        Examples:
        <pre class="code"><code class="java">
        when(mock.someMethod()).thenReturn(10);
        //you can use flexible argument matchers, e.g:
        when(mock.someMethod(anyString())).thenReturn(10);
        //setting exception to be thrown:
        when(mock.someMethod("some arg")).thenThrow(new RuntimeException());
        //you can set different behavior for consecutive method calls.
        //Last stubbing (e.g: thenReturn("foo")) determines the behavior of further consecutive calls.
        when(mock.someMethod("some arg"))
        .thenThrow(new RuntimeException())
        .thenReturn("foo");
        //Alternative, shorter version for consecutive stubbing:
        when(mock.someMethod("some arg"))
        .thenReturn("one", "two");
        //is the same as:
        when(mock.someMethod("some arg"))
        .thenReturn("one")
        .thenReturn("two");
        //shorter version for consecutive method calls throwing exceptions:
        when(mock.someMethod("some arg"))
        .thenThrow(new RuntimeException(), new NullPointerException();
        For stubbing void methods with throwables see: Mockito#doThrow(Throwable...)
        Stubbing can be overridden: for example common stubbing can go to fixture
        setup but the test methods can override it.
        Please note that overridding stubbing is a potential code smell that points out too much stubbing.
        Once stubbed, the method will always return stubbed value regardless
        of how many times it is called.
        Last stubbing is more important - when you stubbed the same method with
        the same arguments many times.
        Although it is possible to verify a stubbed invocation, usually it's just redundant.
        Let's say you've stubbed foo.bar().
        If your code cares what foo.bar() returns then something else breaks(often before even verify() gets executed).
        If your code doesn't care what get(0) returns then it should not be stubbed.
        Not convinced? See <a href="http://monkeyisland.pl/2008/04/26/asking-and-telling">here.
        See examples in javadoc for Mockito class
        @param methodCall method to be stubbed
        @return OngoingStubbing object used to stub fluently.
        Do not create a reference to this returned object.

# File: `SmartPrinter.java`

## Class: `SmartPrinter`

        <!-- META {"entityType": "Class", "entitySignature": "SmartPrinter", "entityFile": "SmartPrinter.java"} -->Makes sure both wanted and actual are printed consistently (single line or multiline)
        Makes arguments printed with types if necessary

# File: `OngoingStubbing.java`

## Method: `OngoingStubbing<T> thenReturn(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> thenReturn(T value)", "entityFile": "OngoingStubbing.java"} -->Sets a return value to be returned when the method is called. E.g:
        <pre class="code"><code class="java">
        when(mock.someMethod()).thenReturn(10);
        See examples in javadoc for Mockito#when
        @param value return value
        @return iOngoingStubbing object that allows stubbing consecutive calls

# File: `Mockito.java`

## Method: `public static T verify(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T verify(T mock)", "entityFile": "Mockito.java"} -->Verifies certain behavior happened once.
        Alias to verify(mock, times(1)) E.g:
        <pre class="code"><code class="java">
        verify(mock).someMethod("some arg");
        Above is equivalent to:
        <pre class="code"><code class="java">
        verify(mock, times(1)).someMethod("some arg");
        Arguments passed are compared using equals() method.
        Read about ArgumentCaptor or ArgumentMatcher to find out other ways of matching / asserting arguments passed.
        Although it is possible to verify a stubbed invocation, usually it's just redundant.
        Let's say you've stubbed foo.bar().
        If your code cares what foo.bar() returns then something else breaks(often before even verify() gets executed).
        If your code doesn't care what get(0) returns then it should not be stubbed.
        Not convinced? See <a href="http://monkeyisland.pl/2008/04/26/asking-and-telling">here.
        See examples in javadoc for Mockito class
        @param mock to be verified
        @return mock object itself

# File: `OngoingStubbing.java`

## Method: `OngoingStubbing<T> thenThrow(Throwable... throwables)`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> thenThrow(Throwable... throwables)", "entityFile": "OngoingStubbing.java"} -->Sets Throwable objects to be thrown when the method is called. E.g:
        <pre class="code"><code class="java">
        when(mock.someMethod()).thenThrow(new RuntimeException());
        If throwables contain a checked exception then it has to
        match one of the checked exceptions of method signature.
        You can specify throwables to be thrown for consecutive calls.
        In that case the last throwable determines the behavior of further consecutive calls.
        If throwable is null then exception will be thrown.
        See examples in javadoc for Mockito#when
        @param throwables to be thrown on method invocation
        @return iOngoingStubbing object that allows stubbing consecutive calls

# File: `InOrder.java`

## Method: `T verify(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "T verify(T mock)", "entityFile": "InOrder.java"} -->Verifies interaction happened once in order.
        Alias to inOrder.verify(mock, times(1))
        Example:
        <pre class="code"><code class="java">
        InOrder inOrder = inOrder(firstMock, secondMock);
        inOrder.verify(firstMock).someMethod("was called first");
        inOrder.verify(secondMock).someMethod("was called second");
        See examples in javadoc for Mockito class
        @param mock to be verified
        @return mock object itself

# File: `Mockito.java`

## Method: `public static T verify(T mock, VerificationMode mode)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T verify(T mock, VerificationMode mode)", "entityFile": "Mockito.java"} -->Verifies certain behavior happened at least once / exact number of times / never. E.g:
        <pre class="code"><code class="java">
        verify(mock, times(5)).someMethod("was called five times");
        verify(mock, atLeast(2)).someMethod("was called at least two times");
        //you can use flexible argument matchers, e.g:
        verify(mock, atLeastOnce()).someMethod(anyString());
        times(1) is the default and can be omitted
        Arguments passed are compared using equals() method.
        Read about ArgumentCaptor or ArgumentMatcher to find out other ways of matching / asserting arguments passed.
        @param mock to be verified
        @param mode times(x), atLeastOnce() or never()
        @return mock object itself

# File: `InOrder.java`

## Method: `T verify(T mock, VerificationMode mode)`

        <!-- META {"entityType": "Method", "entitySignature": "T verify(T mock, VerificationMode mode)", "entityFile": "InOrder.java"} -->Verifies interaction in order. E.g:
        <pre class="code"><code class="java">
        InOrder inOrder = inOrder(firstMock, secondMock);
        inOrder.verify(firstMock, times(2)).someMethod("was called first two times");
        inOrder.verify(secondMock, atLeastOnce()).someMethod("was called second at least once");
        See examples in javadoc for Mockito class
        @param mock to be verified
        @param mode for example times(x) or atLeastOnce()
        @return mock object itself

# File: `OngoingStubbing.java`

## Method: `OngoingStubbing<T> thenThrow(Class<? extends Throwable> throwableType)`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> thenThrow(Class<? extends Throwable> throwableType)", "entityFile": "OngoingStubbing.java"} -->Sets a Throwable type to be thrown when the method is called. E.g:
        <pre class="code"><code class="java">
        when(mock.someMethod()).thenThrow(RuntimeException.class);
        If the throwable class is a checked exception then it has to
        match one of the checked exceptions of the stubbed method signature.
        If throwable is null then exception will be thrown.
        See examples in javadoc for Mockito#when
        @param throwableType to be thrown on method invocation
        @return iOngoingStubbing object that allows stubbing consecutive calls
        @since 2.0.0

# File: `Mockito.java`

## Method: `public static void reset(T... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void reset(T... mocks)", "entityFile": "Mockito.java"} -->Smart Mockito users hardly use this feature because they know it could be a sign of poor tests.
        Normally, you don't need to reset your mocks, just create new mocks for each test method.
        Instead of #reset() please consider writing simple, small and focused test methods over lengthy, over-specified tests.
        First potential code smell is reset() in the middle of the test method. This probably means you're testing too much.
        Follow the whisper of your test methods: "Please keep us small & focused on single behavior".
        There are several threads about it on mockito mailing list.
        The only reason we added reset() method is to
        make it possible to work with container-injected mocks.
        See issue 55 (<a href="http://code.google.com/p/mockito/issues/detail?id=55">here)
        or FAQ (<a href="http://code.google.com/p/mockito/wiki/FAQ">here).
        Don't harm yourself. reset() in the middle of the test method is a code smell (you're probably testing too much).
        <pre class="code"><code class="java">
        List mock = mock(List.class);
        when(mock.size()).thenReturn(10);
        mock.add(1);
        reset(mock);
        //at this point the mock forgot any interactions & stubbing
        @param <T> The Type of the mocks
        @param mocks to be reset

# File: `InOrder.java`

## Method: `void verifyNoMoreInteractions()`

        <!-- META {"entityType": "Method", "entitySignature": "void verifyNoMoreInteractions()", "entityFile": "InOrder.java"} -->Verifies that no more interactions happened in order.
        Different from Mockito#verifyNoMoreInteractions(Object...) because the order of verification matters.
        Example:
        <pre class="code"><code class="java">
        mock.foo(); //1st
        mock.bar(); //2nd
        mock.baz(); //3rd
        InOrder inOrder = inOrder(mock);
        inOrder.verify(mock).bar(); //2n
        inOrder.verify(mock).baz(); //3rd (last method)
        //passes because there are no more interactions after last method:
        inOrder.verifyNoMoreInteractions();
        //however this fails because 1st method was not verified:
        Mockito.verifyNoMoreInteractions(mock);

# File: `OngoingStubbing.java`

## Method: `OngoingStubbing<T> thenCallRealMethod()`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> thenCallRealMethod()", "entityFile": "OngoingStubbing.java"} -->Sets the real implementation to be called when the method is called on a mock object.
        As usual you are going to read the partial mock warning:
        Object oriented programming is more less tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        <pre class="code"><code class="java">
        // someMethod() must be safe (e.g. doesn't throw, doesn't have dependencies to the object state, etc.)
        // if it isn't safe then you will have trouble stubbing it using this api. Use Mockito.doCallRealMethod() instead.
        when(mock.someMethod()).thenCallRealMethod();
        // calls real method:
        mock.someMethod();
        See also javadoc Mockito#spy(Object) to find out more about partial mocks.
        Mockito.spy() is a recommended way of creating partial mocks.
        The reason is it guarantees real methods are called against correctly constructed object because you're responsible for constructing the object passed to spy() method.
        See examples in javadoc for Mockito#when
        @return iOngoingStubbing object that allows stubbing consecutive calls

# File: `InOrder.java`

## Interface: `InOrder`

        <!-- META {"entityType": "Interface", "entitySignature": "InOrder", "entityFile": "InOrder.java"} -->Allows verification in order. E.g:
        <pre class="code"><code class="java">
        InOrder inOrder = inOrder(firstMock, secondMock);
        inOrder.verify(firstMock).add("was called first");
        inOrder.verify(secondMock).add("was called second");
        As of Mockito 1.8.4 you can verifyNoMoreInvocations() in order-sensitive way. Read more: InOrder#verifyNoMoreInteractions()
        See examples in javadoc for Mockito class

# File: `Mockito.java`

## Method: `public static void clearInvocations(T... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void clearInvocations(T... mocks)", "entityFile": "Mockito.java"} -->Use this method in order to only clear invocations, when stubbing is non-trivial. Use-cases can be:
        You are using a dependency injection framework to inject your mocks.
        The mock is used in a stateful scenario. For example a class is Singleton which depends on your mock.
        Try to avoid this method at all costs. Only clear invocations if you are unable to efficiently test your program.
        @param <T> The type of the mocks
        @param mocks The mocks to clear the invocations for

# File: `OngoingStubbing.java`

## Method: `OngoingStubbing<T> thenAnswer(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> thenAnswer(Answer<?> answer)", "entityFile": "OngoingStubbing.java"} -->Sets a generic Answer for the method. E.g:
        <pre class="code"><code class="java">
        when(mock.someMethod(10)).thenAnswer(new Answer&lt;Integer&gt;() {
        public Integer answer(InvocationOnMock invocation) throws Throwable {
        return (Integer) invocation.getArguments()[0];
        }
        }
        @param answer the custom answer to execute.
        @return iOngoingStubbing object that allows stubbing consecutive calls

## Method: `OngoingStubbing<T> then(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "OngoingStubbing<T> then(Answer<?> answer)", "entityFile": "OngoingStubbing.java"} -->Sets a generic Answer for the method.
        This method is an alias of #thenAnswer(Answer). This alias allows
        more readable tests on occasion, for example:
        <pre class="code"><code class="java">
        //using 'then' alias:
        when(mock.foo()).then(returnCoolValue());
        //versus good old 'thenAnswer:
        when(mock.foo()).thenAnswer(byReturningCoolValue());
        @param answer the custom answer to execute.
        @return iOngoingStubbing object that allows stubbing consecutive calls
        @see #thenAnswer(Answer)
        @since 1.9.0

# File: `Mockito.java`

## Method: `public static void verifyNoMoreInteractions(Object... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void verifyNoMoreInteractions(Object... mocks)", "entityFile": "Mockito.java"} -->Checks if any of given mocks has any unverified interaction.
        You can use this method after you verified your mocks - to make sure that nothing
        else was invoked on your mocks.
        See also Mockito#never() - it is more explicit and communicates the intent well.
        Stubbed invocations (if called) are also treated as interactions.
        A word of warning:
        Some users who did a lot of classic, expect-run-verify mocking tend to use verifyNoMoreInteractions() very often, even in every test method.
        verifyNoMoreInteractions() is not recommended to use in every test method.
        verifyNoMoreInteractions() is a handy assertion from the interaction testing toolkit. Use it only when it's relevant.
        Abusing it leads to overspecified, less maintainable tests. You can find further reading
        <a href="http://monkeyisland.pl/2008/07/12/should-i-worry-about-the-unexpected/">here.
        This method will also detect unverified invocations that occurred before the test method,
        for example: in setUp(), @Before method or in constructor.
        Consider writing nice code that makes interactions only in test methods.
        Example:
        <pre class="code"><code class="java">
        //interactions
        mock.doSomething();
        mock.doSomethingUnexpected();
        //verification
        verify(mock).doSomething();
        //following will fail because 'doSomethingUnexpected()' is unexpected
        verifyNoMoreInteractions(mock);
        See examples in javadoc for Mockito class
        @param mocks to be verified

# File: `OngoingStubbing.java`

## Method: `M getMock()`

        <!-- META {"entityType": "Method", "entitySignature": "M getMock()", "entityFile": "OngoingStubbing.java"} -->Returns the mock that was used for this stub.
        It allows to create a stub in one line of code.
        This can be helpful to keep test code clean.
        For example, some boring stub can be created & stubbed at field initialization in a test:
        <pre class="code"><code class="java">
        public class CarTest {
        Car boringStubbedCar = when(mock(Car.class).shiftGear()).thenThrow(EngineNotStarted.class).getMock();
        @Test public void should... {}
        @param <M> The mock type given by the variable type.
        @return Mock used in this ongoing stubbing.
        @since 1.9.0

# File: `Mockito.java`

## Method: `public static void verifyZeroInteractions(Object... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void verifyZeroInteractions(Object... mocks)", "entityFile": "Mockito.java"} -->Verifies that no interactions happened on given mocks.
        <pre class="code"><code class="java">
        verifyZeroInteractions(mockOne, mockTwo);
        This method will also detect invocations
        that occurred before the test method, for example: in setUp(), @Before method or in constructor.
        Consider writing nice code that makes interactions only in test methods.
        See also Mockito#never() - it is more explicit and communicates the intent well.
        See examples in javadoc for Mockito class
        @param mocks to be verified

# File: `OngoingStubbing.java`

## Interface: `OngoingStubbing`

        <!-- META {"entityType": "Interface", "entitySignature": "OngoingStubbing", "entityFile": "OngoingStubbing.java"} -->Simply put: "When the x method is called then return y". E.g:
        <pre class="code"><code class="java">
        when(mock.someMethod()).thenReturn(10);
        //you can use flexible argument matchers, e.g:
        when(mock.someMethod(anyString())).thenReturn(10);
        //setting exception to be thrown:
        when(mock.someMethod("some arg")).thenThrow(new RuntimeException());
        //you can set different behavior for consecutive method calls.
        //Last stubbing (e.g: thenReturn("foo")) determines the behavior of further consecutive calls.
        when(mock.someMethod("some arg"))
        .thenThrow(new RuntimeException())
        .thenReturn("foo");
        //There is a shorter way of consecutive stubbing:
        when(mock.someMethod()).thenReturn(1,2,3);
        when(mock.otherMethod()).thenThrow(exc1, exc2);
        See examples in javadoc for Mockito#when

# File: `ClassPathLoader.java`

## Class: `ClassPathLoader`

        <!-- META {"entityType": "Class", "entitySignature": "ClassPathLoader", "entityFile": "ClassPathLoader.java"} -->Loads configuration or extension points available in the classpath.
        Can load the mockito configuration. The user who want to provide his own mockito configuration
        should write the class org.mockito.configuration.MockitoConfiguration that implements
        IMockitoConfiguration. For example :
        <pre class="code"><code class="java">
        package org.mockito.configuration;
        //...
        public class MockitoConfiguration implements IMockitoConfiguration {
        boolean enableClassCache() { return false; }
        // ...
        }
        Can load available mockito extensions. Currently Mockito only have one extension point the
        MockMaker. This extension point allows a user to provide his own bytecode engine to build mocks.
        Suppose you wrote an extension to create mocks with some Awesome library, in order to tell
        Mockito to use it you need to put in your classpath
        <ol style="list-style-type: lower-alpha">
        The implementation itself, for example org.awesome.mockito.AwesomeMockMaker.
        A file named org.mockito.plugins.MockMaker in a folder named
        mockito-extensions, the content of this file need to have one line with
        the qualified name org.awesome.mockito.AwesomeMockMaker.

# File: `Mockito.java`

## Method: `public static VoidMethodStubbable<T> stubVoid(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VoidMethodStubbable<T> stubVoid(T mock)", "entityFile": "Mockito.java"} --><pre class="code"><code class="java">
        //Instead of:
        stubVoid(mock).toThrow(e).on().someVoidMethod();
        //Please do:
        doThrow(e).when(mock).someVoidMethod();
        doThrow() replaces stubVoid() because of improved readability and consistency with the family of doAnswer() methods.
        Originally, stubVoid() was used for stubbing void methods with exceptions. E.g:
        <pre class="code"><code class="java">
        stubVoid(mock).toThrow(new RuntimeException()).on().someMethod();
        //you can stub with different behavior for consecutive calls.
        //Last stubbing (e.g. toReturn()) determines the behavior for further consecutive calls.
        stubVoid(mock)
        .toThrow(new RuntimeException())
        .toReturn()
        .on().someMethod();
        See examples in javadoc for Mockito class
        @deprecated Use Mockito#doThrow(Throwable...) method for stubbing voids
        @param mock
        to stub
        @return stubbable object that allows stubbing with throwable

## Method: `public static Stubber doThrow(Throwable... toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doThrow(Throwable... toBeThrown)", "entityFile": "Mockito.java"} --><!-- 30eb96d8-1784-11ea-80b8-333445793454 <=< ACCEPT -->Use doThrow() when you want to stub the void method with an exception.
        Stubbing voids requires different approach from Mockito#when(Object) because the compiler
        does not like void methods inside brackets...
        Example:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException()).when(mock).someVoidMethod();
        @param toBeThrown to be thrown when the stubbed method is called
        @return stubber - to select a method for stubbing<!-- ACCEPT >=> 30eb96d8-1784-11ea-80b8-333445793454 -->

## Method: `public static Stubber doThrow(Class<? extends Throwable> toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doThrow(Class<? extends Throwable> toBeThrown)", "entityFile": "Mockito.java"} --><!-- 30eb96d8-1784-11ea-80b8-333445793454 <=< ACCEPT -->Use doThrow() when you want to stub the void method with an exception.
        A new exception instance will be created for each method invocation.
        Stubbing voids requires different approach from Mockito#when(Object) because the compiler
        does not like void methods inside brackets...
        Example:
        <pre class="code"><code class="java">
        doThrow(RuntimeException.class).when(mock).someVoidMethod();
        @param toBeThrown to be thrown when the stubbed method is called
        @return stubber - to select a method for stubbing
        @since 2.0.0<!-- ACCEPT >=> 30eb96d8-1784-11ea-80b8-333445793454 -->

# File: `Stubber.java`

## Method: `T when(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "T when(T mock)", "entityFile": "Stubber.java"} -->Allows to choose a method when stubbing in doThrow()|doAnswer()|doNothing()|doReturn() style
        Example:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException())
        .when(mockedList).clear();
        //following throws RuntimeException:
        mockedList.clear();
        Read more about those methods:
        Mockito#doThrow(Throwable[])
        Mockito#doAnswer(Answer)
        Mockito#doNothing()
        Mockito#doReturn(Object)
        See examples in javadoc for Mockito
        @param mock The mock
        @return select method for stubbing

# File: `DefaultAnnotationEngine.java`

## Class: `DefaultAnnotationEngine`

        <!-- META {"entityType": "Class", "entitySignature": "DefaultAnnotationEngine", "entityFile": "DefaultAnnotationEngine.java"} -->Initializes fields annotated with &#64;org.mockito.Mock or &#64;org.mockito.Captor.
        The #process(Class, Object) method implementation does not process super classes!
        @see MockitoAnnotations

# File: `Stubber.java`

## Method: `Stubber doThrow(Throwable... toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doThrow(Throwable... toBeThrown)", "entityFile": "Stubber.java"} --><!-- cc2ad186-1783-11ea-a61b-333445793454 <=< ACCEPT -->Use it for stubbing consecutive calls in Mockito#doThrow(Throwable[]) style:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException("one")).
        doThrow(new RuntimeException("two"))
        .when(mock).someVoidMethod();
        See javadoc for Mockito#doThrow(Throwable[])
        @param toBeThrown to be thrown when the stubbed method is called
        @return stubber - to select a method for stubbing<!-- ACCEPT >=> cc2ad186-1783-11ea-a61b-333445793454 -->

## Method: `Stubber doThrow(Class<? extends Throwable> toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doThrow(Class<? extends Throwable> toBeThrown)", "entityFile": "Stubber.java"} --><!-- cc2ad186-1783-11ea-a61b-333445793454 <=< ACCEPT -->Use it for stubbing consecutive calls in Mockito#doThrow(Class) style:
        <pre class="code"><code class="java">
        doThrow(RuntimeException.class).
        doThrow(IllegalArgumentException.class)
        .when(mock).someVoidMethod();
        See javadoc for Mockito#doThrow(Class)
        @param toBeThrown exception class to be thrown when the stubbed method is called
        @return stubber - to select a method for stubbing
        @since 2.0.0<!-- ACCEPT >=> cc2ad186-1783-11ea-a61b-333445793454 -->

# File: `DefaultInjectionEngine.java`

## Class: `DefaultInjectionEngine`

        <!-- META {"entityType": "Class", "entitySignature": "DefaultInjectionEngine", "entityFile": "DefaultInjectionEngine.java"} -->Inject mock/spies dependencies for fields annotated with @InjectMocks
        See org.mockito.MockitoAnnotations

# File: `Stubber.java`

## Method: `Stubber doAnswer(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doAnswer(Answer answer)", "entityFile": "Stubber.java"} -->Use it for stubbing consecutive calls in Mockito#doAnswer(Answer) style:
        <pre class="code"><code class="java">
        doAnswer(answerOne).
        doAnswer(answerTwo)
        .when(mock).someVoidMethod();
        See javadoc for Mockito#doAnswer(Answer)
        @param answer to answer when the stubbed method is called
        @return stubber - to select a method for stubbing

# File: `Mockito.java`

## Method: `public static Stubber doCallRealMethod()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doCallRealMethod()", "entityFile": "Mockito.java"} -->Use doCallRealMethod() when you want to call the real implementation of a method.
        As usual you are going to read the partial mock warning:
        Object oriented programming is more less tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        See also javadoc Mockito#spy(Object) to find out more about partial mocks.
        Mockito.spy() is a recommended way of creating partial mocks.
        The reason is it guarantees real methods are called against correctly constructed object because you're responsible for constructing the object passed to spy() method.
        Example:
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class);
        doCallRealMethod().when(mock).someVoidMethod();
        // this will call the real implementation of Foo.someVoidMethod()
        mock.someVoidMethod();
        See examples in javadoc for Mockito class
        @return stubber - to select a method for stubbing
        @since 1.9.5

# File: `Stubber.java`

## Method: `Stubber doNothing()`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doNothing()", "entityFile": "Stubber.java"} -->Use it for stubbing consecutive calls in Mockito#doNothing() style:
        <pre class="code"><code class="java">
        doNothing().
        doThrow(new RuntimeException("two"))
        .when(mock).someVoidMethod();
        See javadoc for Mockito#doNothing()
        @return stubber - to select a method for stubbing

# File: `Mockito.java`

## Method: `public static Stubber doAnswer(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doAnswer(Answer answer)", "entityFile": "Mockito.java"} -->Use doAnswer() when you want to stub a void method with generic Answer.
        Stubbing voids requires different approach from Mockito#when(Object) because the compiler does not like void methods inside brackets...
        Example:
        <pre class="code"><code class="java">
        doAnswer(new Answer() {
        public Object answer(InvocationOnMock invocation) {
        Object[] args = invocation.getArguments();
        Mock mock = invocation.getMock();
        return null;
        }})
        .when(mock).someMethod();
        See examples in javadoc for Mockito class
        @param answer to answer when the stubbed method is called
        @return stubber - to select a method for stubbing

# File: `Stubber.java`

## Method: `Stubber doReturn(Object toBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doReturn(Object toBeReturned)", "entityFile": "Stubber.java"} -->Use it for stubbing consecutive calls in Mockito#doReturn(Object) style.
        See javadoc for Mockito#doReturn(Object)
        @param toBeReturned to be returned when the stubbed method is called
        @return stubber - to select a method for stubbing

## Method: `Stubber doReturn(Object toBeReturned, Object... nextToBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doReturn(Object toBeReturned, Object... nextToBeReturned)", "entityFile": "Stubber.java"} -->Use it for stubbing consecutive calls in Mockito#doReturn(Object) style.
        See javadoc for Mockito#doReturn(Object, Object...)
        @param toBeReturned to be returned when the stubbed method is called
        @param nextToBeReturned to be returned in consecutive calls when the stubbed method is called
        @return stubber - to select a method for stubbing

## Method: `Stubber doCallRealMethod()`

        <!-- META {"entityType": "Method", "entitySignature": "Stubber doCallRealMethod()", "entityFile": "Stubber.java"} -->Use it for stubbing consecutive calls in Mockito#doCallRealMethod() style.
        See javadoc for Mockito#doCallRealMethod()
        @return stubber - to select a method for stubbing

# File: `Mockito.java`

## Method: `public static Stubber doNothing()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doNothing()", "entityFile": "Mockito.java"} -->Use doNothing() for setting void methods to do nothing. Beware that void methods on mocks do nothing by default!
        However, there are rare situations when doNothing() comes handy:
        Stubbing consecutive calls on a void method:
        <pre class="code"><code class="java">
        doNothing().
        doThrow(new RuntimeException())
        .when(mock).someVoidMethod();
        //does nothing the first time:
        mock.someVoidMethod();
        //throws RuntimeException the next time:
        mock.someVoidMethod();
        When you spy real objects and you want the void method to do nothing:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //let's make clear() do nothing
        doNothing().when(spy).clear();
        spy.add("one");
        //clear() does nothing, so the list still contains "one"
        spy.clear();
        See examples in javadoc for Mockito class
        @return stubber - to select a method for stubbing

# File: `Stubber.java`

## Interface: `Stubber`

        <!-- META {"entityType": "Interface", "entitySignature": "Stubber", "entityFile": "Stubber.java"} -->Allows to choose a method when stubbing in doThrow()|doAnswer()|doNothing()|doReturn() style
        Example:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException()).when(mockedList).clear();
        //following throws RuntimeException:
        mockedList.clear();
        Also useful when stubbing consecutive calls:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException("one")).
        doThrow(new RuntimeException("two"))
        .when(mock).someVoidMethod();
        Read more about those methods:
        Mockito#doThrow(Throwable[])
        Mockito#doAnswer(Answer)
        Mockito#doNothing()
        Mockito#doReturn(Object)
        See examples in javadoc for Mockito

# File: `GlobalConfiguration.java`

## Class: `GlobalConfiguration`

        <!-- META {"entityType": "Class", "entitySignature": "GlobalConfiguration", "entityFile": "GlobalConfiguration.java"} -->Thread-safe wrapper on user-defined org.mockito.configuration.MockitoConfiguration implementation

# File: `Mockito.java`

## Method: `public static Stubber doReturn(Object toBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doReturn(Object toBeReturned)", "entityFile": "Mockito.java"} -->Use doReturn() in those rare occasions when you cannot use Mockito#when(Object).
        Beware that Mockito#when(Object) is always recommended for stubbing because it is argument type-safe
        and more readable (especially when stubbing consecutive calls).
        Here are those rare occasions when doReturn() comes handy:
        When spying real objects and calling real methods on a spy brings side effects
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing:
        doReturn("foo").when(spy).get(0);
        Overriding a previous exception-stubbing:
        <pre class="code"><code class="java">
        when(mock.foo()).thenThrow(new RuntimeException());
        //Impossible: the exception-stubbed foo() method is called so RuntimeException is thrown.
        when(mock.foo()).thenReturn("bar");
        //You have to use doReturn() for stubbing:
        doReturn("bar").when(mock).foo();
        Above scenarios shows a tradeoff of Mockito's elegant syntax. Note that the scenarios are very rare, though.
        Spying should be sporadic and overriding exception-stubbing is very rare. Not to mention that in general
        overridding stubbing is a potential code smell that points out too much stubbing.
        See examples in javadoc for Mockito class
        @param toBeReturned to be returned when the stubbed method is called
        @return stubber - to select a method for stubbing

# File: `VoidMethodStubbable.java`

## Method: `VoidMethodStubbable<T> toThrow(Throwable throwable)`

        <!-- META {"entityType": "Method", "entitySignature": "VoidMethodStubbable<T> toThrow(Throwable throwable)", "entityFile": "VoidMethodStubbable.java"} -->Stubs void method with an exception. E.g:
        <pre class="code"><code class="java">
        stubVoid(mock).toThrow(new RuntimeException()).on().someMethod();
        If throwable is a checked exception then it has to
        match one of the checked exceptions of method signature.
        See examples in javadoc for Mockito#stubVoid
        @param throwable to be thrown on method invocation
        @return VoidMethodStubbable - typically to choose void method and finish stubbing

# File: `InjectingAnnotationEngine.java`

## Method: `public Object createMockFor(Annotation annotation, Field field)`

        <!-- META {"entityType": "Method", "entitySignature": "public Object createMockFor(Annotation annotation, Field field)", "entityFile": "InjectingAnnotationEngine.java"} -->*
        Create a mock using DefaultAnnotationEngine
        @see org.mockito.internal.configuration.DefaultAnnotationEngine
        @see org.mockito.configuration.AnnotationEngine#createMockFor(java.lang.annotation.Annotation, java.lang.reflect.Field)

## Method: `public void process(Class<?> clazz, Object testInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "public void process(Class<?> clazz, Object testInstance)", "entityFile": "InjectingAnnotationEngine.java"} -->Process the fields of the test instance and create Mocks, Spies, Captors and inject them on fields
        annotated &#64;InjectMocks.
        This code process the test class and the super classes.
        First create Mocks, Spies, Captors.
        Then try to inject them.
        @param clazz Not used
        @param testInstance The instance of the test, should not be null.
        @see org.mockito.configuration.AnnotationEngine#process(Class, Object)

## Method: `public void injectMocks(final Object testClassInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "public void injectMocks(final Object testClassInstance)", "entityFile": "InjectingAnnotationEngine.java"} -->Initializes mock/spies dependencies for objects annotated with
        @InjectMocks for given testClassInstance.
        See examples in javadoc for MockitoAnnotations class.
        @param testClassInstance
        Test class, usually this

# File: `VoidMethodStubbable.java`

## Method: `VoidMethodStubbable<T> toReturn()`

        <!-- META {"entityType": "Method", "entitySignature": "VoidMethodStubbable<T> toReturn()", "entityFile": "VoidMethodStubbable.java"} -->Stubs void method to 'just return' (e.g. to not to throw any exception)
        Only use this method if you're stubbing consecutive calls.
        For example:
        <pre class="code"><code class="java">
        stubVoid(mock)
        .toReturn()
        .toThrow(new RuntimeException())
        .on().foo(10);
        first time foo(10) is called the mock will 'just return' (e.g. don't throw any exception)
        second time foo(10) is called the mock will throw RuntimeException
        every consecutive time foo(10) is called the mock will throw RuntimeException
        See examples in javadoc for Mockito#stubVoid
        @return VoidMethodStubbable - typically to choose void method and finish stubbing

## Method: `VoidMethodStubbable<T> toAnswer(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "VoidMethodStubbable<T> toAnswer(Answer<?> answer)", "entityFile": "VoidMethodStubbable.java"} -->Stubs a void method with generic Answer
        For Example:
        <pre class="code"><code class="java">
        stubVoid(mock)
        .toAnswer(new Answer() {
        public Object answer(InvocationOnMOck invocation) {
        Visitor v = (Visitor) invocation.getArguments()[0];
        v.visitMock(invocation.getMock());
        return null;
        }
        })
        .on().accept(any());
        @param answer the custom answer to execute.
        @return VoidMethodStubbable - typically to choose void method and finish stubbing

# File: `Mockito.java`

## Method: `public static Stubber doReturn(Object toBeReturned, Object... toBeReturnedNext)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Stubber doReturn(Object toBeReturned, Object... toBeReturnedNext)", "entityFile": "Mockito.java"} -->Same as #doReturn(Object) but sets consecutive values to be returned. Remember to use
        doReturn() in those rare occasions when you cannot use Mockito#when(Object).
        Beware that Mockito#when(Object) is always recommended for stubbing because it is argument type-safe
        and more readable (especially when stubbing consecutive calls).
        Here are those rare occasions when doReturn() comes handy:
        When spying real objects and calling real methods on a spy brings side effects
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo", "bar", "qix");
        //You have to use doReturn() for stubbing:
        doReturn("foo", "bar", "qix").when(spy).get(0);
        Overriding a previous exception-stubbing:
        <pre class="code"><code class="java">
        when(mock.foo()).thenThrow(new RuntimeException());
        //Impossible: the exception-stubbed foo() method is called so RuntimeException is thrown.
        when(mock.foo()).thenReturn("bar", "foo", "qix");
        //You have to use doReturn() for stubbing:
        doReturn("bar", "foo", "qix").when(mock).foo();
        Above scenarios shows a trade-off of Mockito's elegant syntax. Note that the scenarios are very rare, though.
        Spying should be sporadic and overriding exception-stubbing is very rare. Not to mention that in general
        overridding stubbing is a potential code smell that points out too much stubbing.
        See examples in javadoc for Mockito class
        @param toBeReturned to be returned when the stubbed method is called
        @param toBeReturnedNext to be returned in consecutive calls when the stubbed method is called
        @return stubber - to select a method for stubbing
        @since 2.0.0

# File: `VoidMethodStubbable.java`

## Method: `T on()`

        <!-- META {"entityType": "Method", "entitySignature": "T on()", "entityFile": "VoidMethodStubbable.java"} -->Choose void method for stubbing. E.g:
        <pre class="code"><code class="java">
        stubVoid(mock).toThrow(new RuntimeException()).on().someMethod("some arg");
        See examples in javadoc for Mockito#stubVoid
        @return mock object itself

# File: `ConstructorInjection.java`

## Class: `SimpleArgumentResolver`

        <!-- META {"entityType": "Class", "entitySignature": "SimpleArgumentResolver", "entityFile": "ConstructorInjection.java"} -->Returns mocks that match the argument type, if not possible assigns null.

## Class: `ConstructorInjection`

        <!-- META {"entityType": "Class", "entitySignature": "ConstructorInjection", "entityFile": "ConstructorInjection.java"} -->Injection strategy based on constructor.
        The strategy will search for the constructor with most parameters
        and try to resolve mocks by type.
        TODO on missing mock type, shall it abandon or create "noname" mocks.
        TODO and what if the arg type is not mockable.
        For now the algorithm tries to create anonymous mocks if an argument type is missing.
        If not possible the algorithm abandon resolution.

# File: `VoidMethodStubbable.java`

## Interface: `VoidMethodStubbable`

        <!-- META {"entityType": "Interface", "entitySignature": "VoidMethodStubbable", "entityFile": "VoidMethodStubbable.java"} -->Stubs void method with an exception. E.g:
        <pre class="code"><code class="java">
        stubVoid(mock).toThrow(new RuntimeException()).on().someMethod();
        //you can stub with different behavior for consecutive method calls.
        //Last stubbing (e.g: toReturn()) determines the behavior for further consecutive calls.
        stubVoid(mock)
        .toThrow(new RuntimeException())
        .toReturn()
        .on().someMethod();
        See examples in javadoc for Mockito#stubVoid

# File: `Mockito.java`

## Method: `public static InOrder inOrder(Object... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static InOrder inOrder(Object... mocks)", "entityFile": "Mockito.java"} -->Creates org.mockito.InOrder object that allows verifying mocks in order.
        <pre class="code"><code class="java">
        InOrder inOrder = inOrder(firstMock, secondMock);
        inOrder.verify(firstMock).add("was called first");
        inOrder.verify(secondMock).add("was called second");
        Verification in order is flexible - you don't have to verify all interactions one-by-one
        but only those that you are interested in testing in order.
        Also, you can create InOrder object passing only mocks that are relevant for in-order verification.
        InOrder verification is 'greedy'. You will hardly every notice it but
        if you want to find out more search for 'greedy' on the Mockito
        <a href="http://code.google.com/p/mockito/w/list">wiki pages.
        As of Mockito 1.8.4 you can verifyNoMoreInvocations() in order-sensitive way. Read more: InOrder#verifyNoMoreInteractions()
        See examples in javadoc for Mockito class
        @param mocks to be verified in order
        @return InOrder object to be used to verify in order

# File: `After.java`

## Method: `public After(long delayMillis, VerificationMode verificationMode)`

        <!-- META {"entityType": "Method", "entitySignature": "public After(long delayMillis, VerificationMode verificationMode)", "entityFile": "After.java"} -->See the javadoc for VerificationAfterDelay
        Typically, you won't use this class explicitly. Instead use timeout() method on Mockito class.
        See javadoc for VerificationWithTimeout

## Class: `After`

        <!-- META {"entityType": "Class", "entitySignature": "After", "entityFile": "After.java"} -->See the javadoc for VerificationAfterDelay
        Typically, you won't use this class explicitly. Instead use timeout() method on Mockito class.
        See javadoc for VerificationWithTimeout

# File: `OngoingInjector.java`

## Method: `Object thenInject()`

        <!-- META {"entityType": "Method", "entitySignature": "Object thenInject()", "entityFile": "OngoingInjector.java"} -->Inject the mock.
        Please check the actual implementation.
        @return the mock that was injected, null otherwise.

# File: `Mockito.java`

## Method: `public static Object[] ignoreStubs(Object... mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Object[] ignoreStubs(Object... mocks)", "entityFile": "Mockito.java"} -->Ignores stubbed methods of given mocks for the sake of verification.
        Sometimes useful when coupled with verifyNoMoreInteractions() or verification inOrder().
        Helps avoiding redundant verification of stubbed calls - typically we're not interested in verifying stubs.
        Warning, ignoreStubs() might lead to overuse of verifyNoMoreInteractions(ignoreStubs(...));
        Bear in mind that Mockito does not recommend bombarding every test with verifyNoMoreInteractions()
        for the reasons outlined in javadoc for Mockito#verifyNoMoreInteractions(Object...)
        Other words: all *stubbed* methods of given mocks are marked *verified* so that they don't get in a way during verifyNoMoreInteractions().
        This method changes the input mocks! This method returns input mocks just for convenience.
        Ignored stubs will also be ignored for verification inOrder, including org.mockito.InOrder#verifyNoMoreInteractions().
        See the second example.
        Example:
        <pre class="code"><code class="java">
        //mocking lists for the sake of the example (if you mock List in real you will burn in hell)
        List mock1 = mock(List.class), mock2 = mock(List.class);
        //stubbing mocks:
        when(mock1.get(0)).thenReturn(10);
        when(mock2.get(0)).thenReturn(20);
        //using mocks by calling stubbed get(0) methods:
        System.out.println(mock1.get(0)); //prints 10
        System.out.println(mock2.get(0)); //prints 20
        //using mocks by calling clear() methods:
        mock1.clear();
        mock2.clear();
        //verification:
        verify(mock1).clear();
        verify(mock2).clear();
        //verifyNoMoreInteractions() fails because get() methods were not accounted for.
        try { verifyNoMoreInteractions(mock1, mock2); } catch (NoInteractionsWanted e);
        //However, if we ignore stubbed methods then we can verifyNoMoreInteractions()
        verifyNoMoreInteractions(ignoreStubs(mock1, mock2));
        //Remember that ignoreStubs() *changes* the input mocks and returns them for convenience.
        Ignoring stubs can be used with verification in order:
        <pre class="code"><code class="java">
        List list = mock(List.class);
        when(mock.get(0)).thenReturn("foo");
        list.add(0);
        System.out.println(list.get(0)); //we don't want to verify this
        list.clear();
        InOrder inOrder = inOrder(ignoreStubs(list));
        inOrder.verify(list).add(0);
        inOrder.verify(list).clear();
        inOrder.verifyNoMoreInteractions();
        @since 1.9.0
        @param mocks input mocks that will be changed
        @return the same mocks that were passed in as parameters

# File: `OngoingInjector.java`

## Field: `nop`

        <!-- META {"entityType": "Field", "entitySignature": "nop", "entityFile": "OngoingInjector.java"} -->Injector that will do nothing, and will return null as no mocks will be injected

# File: `Mockito.java`

## Method: `public static VerificationMode times(int wantedNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode times(int wantedNumberOfInvocations)", "entityFile": "Mockito.java"} --><!-- 77fc6a36-1785-11ea-89bb-333445793454 <=< ACCEPT -->Allows verifying exact number of invocations. E.g:
        <pre class="code"><code class="java">
        verify(mock, times(2)).someMethod("some arg");
        See examples in javadoc for Mockito class
        @param wantedNumberOfInvocations wanted number of invocations
        @return verification mode<!-- ACCEPT >=> 77fc6a36-1785-11ea-89bb-333445793454 -->

## Method: `public static VerificationMode never()`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode never()", "entityFile": "Mockito.java"} -->Alias to times(0), see Mockito#times(int)
        Verifies that interaction did not happen. E.g:
        <pre class="code"><code class="java">
        verify(mock, never()).someMethod();
        If you want to verify there were NO interactions with the mock
        check out Mockito#verifyZeroInteractions(Object...)
        or Mockito#verifyNoMoreInteractions(Object...)
        See examples in javadoc for Mockito class
        @return verification mode

## Method: `public static VerificationMode atLeastOnce()`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode atLeastOnce()", "entityFile": "Mockito.java"} -->Allows at-least-once verification. E.g:
        <pre class="code"><code class="java">
        verify(mock, atLeastOnce()).someMethod("some arg");
        Alias to atLeast(1).
        See examples in javadoc for Mockito class
        @return verification mode

## Method: `public static VerificationMode atLeast(int minNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode atLeast(int minNumberOfInvocations)", "entityFile": "Mockito.java"} --><!-- 77fc6a36-1784-11ea-89bb-333445793454 <=< ACCEPT -->Allows at-least-x verification. E.g:
        <pre class="code"><code class="java">
        verify(mock, atLeast(3)).someMethod("some arg");
        See examples in javadoc for Mockito class
        @param minNumberOfInvocations minimum number of invocations
        @return verification mode<!-- ACCEPT >=> 77fc6a36-1784-11ea-89bb-333445793454 -->

## Method: `public static VerificationMode atMost(int maxNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode atMost(int maxNumberOfInvocations)", "entityFile": "Mockito.java"} --><!-- 77fc6a36-1784-11ea-89bb-333445793454 <=< ACCEPT -->Allows at-most-x verification. E.g:
        <pre class="code"><code class="java">
        verify(mock, atMost(3)).someMethod("some arg");
        See examples in javadoc for Mockito class
        @param maxNumberOfInvocations max number of invocations
        @return verification mode<!-- ACCEPT >=> 77fc6a36-1784-11ea-89bb-333445793454 -->

# File: `Timeout.java`

## Method: `public Timeout(long millis, VerificationMode delegate)`

        <!-- META {"entityType": "Method", "entitySignature": "public Timeout(long millis, VerificationMode delegate)", "entityFile": "Timeout.java"} -->See the javadoc for VerificationWithTimeout
        Typically, you won't use this class explicitly. Instead use timeout() method on Mockito class.
        See javadoc for VerificationWithTimeout

# File: `TerminalMockCandidateFilter.java`

## Class: `TerminalMockCandidateFilter`

        <!-- META {"entityType": "Class", "entitySignature": "TerminalMockCandidateFilter", "entityFile": "TerminalMockCandidateFilter.java"} -->This node returns an actual injecter which will be either :
        an OngoingInjector that do nothing if a candidate couldn't be found
        an OngoingInjector that will try to inject the candidate trying first the property setter then if not possible try the field access

# File: `Timeout.java`

## Class: `Timeout`

        <!-- META {"entityType": "Class", "entitySignature": "Timeout", "entityFile": "Timeout.java"} -->See the javadoc for VerificationWithTimeout
        Typically, you won't use this class explicitly. Instead use timeout() method on Mockito class.
        See javadoc for VerificationWithTimeout

# File: `Mockito.java`

## Method: `public static VerificationMode calls(int wantedNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode calls(int wantedNumberOfInvocations)", "entityFile": "Mockito.java"} -->Allows non-greedy verification in order.  For example
        <pre class="code"><code class="java">
        inOrder.verify( mock, calls( 2 )).someMethod( "some arg" );
        will not fail if the method is called 3 times, unlike times( 2 )
        will not mark the third invocation as verified, unlike atLeast( 2 )
        This verification mode can only be used with in order verification.
        @param wantedNumberOfInvocations number of invocations to verify
        @return  verification mode

# File: `VerificationAfterDelay.java`

## Method: `public VerificationMode times(int wantedNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode times(int wantedNumberOfInvocations)", "entityFile": "VerificationAfterDelay.java"} -->Verifies that there are exactly N invocations during the given period. This will wait the full period given.

## Method: `public VerificationMode never()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode never()", "entityFile": "VerificationAfterDelay.java"} -->Allows verification that there are no invocations at any point during the given period. This will wait the
        full period given, unless an invocation occurs (in which case there will be immediate failure)

## Method: `public VerificationMode atLeastOnce()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atLeastOnce()", "entityFile": "VerificationAfterDelay.java"} -->Verifies that there is at least 1 invocation during the given period. This will wait the full period given.

## Method: `public VerificationMode atLeast(int minNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atLeast(int minNumberOfInvocations)", "entityFile": "VerificationAfterDelay.java"} -->Verifies that there is are least N invocations during the given period. This will wait the full period given.

## Method: `public VerificationMode atMost(int maxNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atMost(int maxNumberOfInvocations)", "entityFile": "VerificationAfterDelay.java"} -->Verifies that there is are most N invocations during the given period. This will wait the full period given,
        unless too many invocations occur (in which case there will be an immediate failure)

## Method: `public VerificationMode only()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode only()", "entityFile": "VerificationAfterDelay.java"} -->Verifies that there the given method is invoked and is the only method invoked. This will wait the full
        period given, unless another method is invoked (in which case there will be an immediate failure)

## Interface: `VerificationAfterDelay`

        <!-- META {"entityType": "Interface", "entitySignature": "VerificationAfterDelay", "entityFile": "VerificationAfterDelay.java"} -->VerificationAfterDelay is a VerificationMode that allows combining existing verification modes with an initial delay, e.g.
        <pre class="code"><code class="java">
        verify(mock, after(100).atMost(5)).foo();
        verify(mock, after(100).never()).bar();
        verify(mock, after(200).atLeastOnce()).baz();
        This is similar to VerificationWithTimeout timeout() except the assertion will not terminate until either the condition is
        definitively failed, or the full time has elapsed (whereas timeout() will also stop if the conditions is true at any point, as is
        typically the case with never() etc initially).
        See examples in javadoc for Mockito#verify(Object, VerificationMode)

# File: `Mockito.java`

## Method: `public static VerificationMode only()`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode only()", "entityFile": "Mockito.java"} --><!-- 0078b26c-1785-11ea-a13e-333445793454 <=< ACCEPT -->Allows checking if given method was the only one invoked. E.g:
        <pre class="code"><code class="java">
        verify(mock, only()).someMethod();
        //above is a shorthand for following 2 lines of code:
        verify(mock).someMethod();
        verifyNoMoreInvocations(mock);
        See also Mockito#verifyNoMoreInteractions(Object...)
        See examples in javadoc for Mockito class
        @return verification mode<!-- ACCEPT >=> 0078b26c-1785-11ea-a13e-333445793454 -->

# File: `VerificationMode.java`

## Method: `VerificationMode description(String description)`

        <!-- META {"entityType": "Method", "entitySignature": "VerificationMode description(String description)", "entityFile": "VerificationMode.java"} -->Description will be prepended to the assertion error if verification fails.
        @param description The custom failure message
        @return VerificationMode
        @since 2.0.0

# File: `MockInjection.java`

## Method: `public static OngoingMockInjection onField(Field field, Object ofInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "public static OngoingMockInjection onField(Field field, Object ofInstance)", "entityFile": "MockInjection.java"} -->Create a new configuration setup for a field
        @param field Field needing mock injection
        @param ofInstance Instance owning the field
        @return New configuration builder

# File: `VerificationMode.java`

## Interface: `VerificationMode`

        <!-- META {"entityType": "Interface", "entitySignature": "VerificationMode", "entityFile": "VerificationMode.java"} -->Allows verifying that certain behavior happened at least once / exact number
        of times / never. E.g:
        <pre class="code"><code class="java">
        verify(mock, times(5)).someMethod(&quot;was called five times&quot;);
        verify(mock, never()).someMethod(&quot;was never called&quot;);
        verify(mock, atLeastOnce()).someMethod(&quot;was called at least once&quot;);
        verify(mock, atLeast(2)).someMethod(&quot;was called at least twice&quot;);
        verify(mock, atMost(3)).someMethod(&quot;was called at most 3 times&quot;);
        times(1) is the default and can be omitted
        See examples in javadoc for Mockito#verify(Object, VerificationMode)

# File: `MockInjection.java`

## Method: `public static OngoingMockInjection onFields(Set<Field> fields, Object ofInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "public static OngoingMockInjection onFields(Set<Field> fields, Object ofInstance)", "entityFile": "MockInjection.java"} -->Create a new configuration setup for fields
        @param fields Fields needing mock injection
        @param ofInstance Instance owning the field
        @return New configuration builder

# File: `Mockito.java`

## Method: `public static VerificationWithTimeout timeout(long millis)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationWithTimeout timeout(long millis)", "entityFile": "Mockito.java"} -->Allows verifying with timeout. It causes a verify to wait for a specified period of time for a desired
        interaction rather than fails immediately if has not already happened. May be useful for testing in concurrent
        conditions.
        This differs from Mockito#after after() in that after() will wait the full period, unless
        the final test result is known early (e.g. if a never() fails), whereas timeout() will stop early as soon
        as verification passes, producing different behaviour when used with times(2), for example, which can pass
        and then later fail. In that case, timeout would pass as soon as times(2) passes, whereas after would run until
        times(2) failed, and then fail.
        It feels this feature should be used rarely - figure out a better way of testing your multi-threaded system
        Not yet implemented to work with InOrder verification.
        <pre class="code"><code class="java">
        //passes when someMethod() is called within given time span
        verify(mock, timeout(100)).someMethod();
        //above is an alias to:
        verify(mock, timeout(100).times(1)).someMethod();
        //passes as soon as someMethod() has been called 2 times before the given timeout
        verify(mock, timeout(100).times(2)).someMethod();
        //equivalent: this also passes as soon as someMethod() has been called 2 times before the given timeout
        verify(mock, timeout(100).atLeast(2)).someMethod();
        //verifies someMethod() within given time span using given verification mode
        //useful only if you have your own custom verification modes.
        verify(mock, new Timeout(100, yourOwnVerificationMode)).someMethod();
        See examples in javadoc for Mockito class
        @param millis - time span in milliseconds
        @return verification mode

## Method: `public static VerificationAfterDelay after(long millis)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationAfterDelay after(long millis)", "entityFile": "Mockito.java"} -->Allows verifying over a given period. It causes a verify to wait for a specified period of time for a desired
        interaction rather than failing immediately if has not already happened. May be useful for testing in concurrent
        conditions.
        This differs from Mockito#timeout timeout() in that after() will wait the full period, whereas timeout()
        will stop early as soon as verification passes, producing different behaviour when used with times(2), for example,
        which can pass and then later fail. In that case, timeout would pass as soon as times(2) passes, whereas after would
        run the full time, which point it will fail, as times(2) has failed.
        It feels this feature should be used rarely - figure out a better way of testing your multi-threaded system
        Not yet implemented to work with InOrder verification.
        <pre class="code"><code class="java">
        //passes after 100ms, if someMethod() has only been called once at that time.
        verify(mock, after(100)).someMethod();
        //above is an alias to:
        verify(mock, after(100).times(1)).someMethod();
        //passes if someMethod() is called *exactly* 2 times after the given timespan
        verify(mock, after(100).times(2)).someMethod();
        //passes if someMethod() has not been called after the given timespan
        verify(mock, after(100).never()).someMethod();
        //verifies someMethod() after a given time span using given verification mode
        //useful only if you have your own custom verification modes.
        verify(mock, new After(100, yourOwnVerificationMode)).someMethod();
        See examples in javadoc for Mockito class
        @param millis - time span in milliseconds
        @return verification mode

# File: `MockInjection.java`

## Class: `MockInjection`

        <!-- META {"entityType": "Class", "entitySignature": "MockInjection", "entityFile": "MockInjection.java"} -->Internal injection configuration utility.
        Allow the user of this class to configure the way the injection of mocks will happen.

# File: `MockInjectionStrategy.java`

## Method: `public MockInjectionStrategy thenTry(MockInjectionStrategy strategy)`

        <!-- META {"entityType": "Method", "entitySignature": "public MockInjectionStrategy thenTry(MockInjectionStrategy strategy)", "entityFile": "MockInjectionStrategy.java"} -->Enqueue next injection strategy.
        The implementation should take care of the actual calling if required.
        @param strategy Queued strategy.
        @return The passed strategy instance to allow chaining.

## Method: `public boolean process(Field onField, Object fieldOwnedBy, Set<Object> mockCandidates)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean process(Field onField, Object fieldOwnedBy, Set<Object> mockCandidates)", "entityFile": "MockInjectionStrategy.java"} -->Actually inject mockCandidates on field.
        Actual algorithm is defined in the implementations of #processInjection(Field, Object, Set).
        However if injection occurred successfully, the process should return true,
        and false otherwise.
        The code takes care of calling the next strategy if available and if of course if required
        @param onField Field needing injection.
        @param fieldOwnedBy The owning instance of the field.
        @param mockCandidates A set of mock candidate, that might be injected.
        @return true if successful, false otherwise.

## Method: `protected abstract boolean processInjection(Field field, Object fieldOwner, Set<Object> mockCandidates)`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract boolean processInjection(Field field, Object fieldOwner, Set<Object> mockCandidates)", "entityFile": "MockInjectionStrategy.java"} -->Process actual injection.
        Don't call this method directly, instead call #process(Field, Object, Set)
        @param field Field needing injection
        @param fieldOwner Field owner instance.
        @param mockCandidates Pool of mocks to inject.
        @return true if injection occurred, false otherwise

# File: `VerificationWithTimeout.java`

## Method: `public VerificationMode times(int wantedNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode times(int wantedNumberOfInvocations)", "entityFile": "VerificationWithTimeout.java"} --><!-- 77fc6a36-1785-11ea-89bb-333445793454 <=< ACCEPT -->Allows verifying exact number of invocations within given timeout
        <pre class="code"><code class="java">
        verify(mock, timeout(100).times(2)).someMethod("some arg");
        See examples in javadoc for Mockito class
        @param wantedNumberOfInvocations wanted number of invocations
        @return verification mode<!-- ACCEPT >=> 77fc6a36-1785-11ea-89bb-333445793454 -->

## Method: `public VerificationMode never()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode never()", "entityFile": "VerificationWithTimeout.java"} --><!-- c2fdafe2-1784-11ea-806e-333445793454 <=< ACCEPT -->@deprecated
        Validation with timeout combined with never simply does not make sense, as never() will typically immediately pass,
        and therefore not wait the timeout. The behaviour you may be looking for is actually provided by after().never().
        To avoid compilation errors upon upgrade the method is deprecated and it throws a "friendly reminder" exception.
        In a future release we will remove timeout(x).atMost(y) and timeout(x).never() from the API.
        Do you want to find out more? See <a href="http://code.google.com/p/mockito/issues/detail?id=235">issue 235
        @return verification mode<!-- ACCEPT >=> c2fdafe2-1784-11ea-806e-333445793454 -->

## Method: `public VerificationMode atLeastOnce()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atLeastOnce()", "entityFile": "VerificationWithTimeout.java"} -->Allows at-least-once verification within given timeout. E.g:
        <pre class="code"><code class="java">
        verify(mock, timeout(100).atLeastOnce()).someMethod("some arg");
        Alias to atLeast(1)
        See examples in javadoc for Mockito class
        @return verification mode

# File: `Mockito.java`

## Method: `public static void validateMockitoUsage()`

        <!-- META {"entityType": "Method", "entitySignature": "public static void validateMockitoUsage()", "entityFile": "Mockito.java"} -->First of all, in case of any trouble, I encourage you to read the Mockito FAQ: <a href="http://code.google.com/p/mockito/wiki/FAQ">http://code.google.com/p/mockito/wiki/FAQ
        In case of questions you may also post to mockito mailing list: <a href="http://groups.google.com/group/mockito">http://groups.google.com/group/mockito
        validateMockitoUsage() explicitly validates the framework state to detect invalid use of Mockito.
        However, this feature is optional because Mockito validates the usage all the time... but there is a gotcha so read on.
        Examples of incorrect use:
        <pre class="code"><code class="java">
        //Oops, thenReturn() part is missing:
        when(mock.get());
        //Oops, verified method call is inside verify() where it should be on the outside:
        verify(mock.execute());
        //Oops, missing method to verify:
        verify(mock);
        Mockito throws exceptions if you misuse it so that you know if your tests are written correctly.
        The gotcha is that Mockito does the validation next time you use the framework (e.g. next time you verify, stub, call mock etc.).
        But even though the exception might be thrown in the next test,
        the exception message contains a navigable stack trace element with location of the defect.
        Hence you can click and find the place where Mockito was misused.
        Sometimes though, you might want to validate the framework usage explicitly.
        For example, one of the users wanted to put validateMockitoUsage() in his @After method
        so that he knows immediately when he misused Mockito.
        Without it, he would have known about it not sooner than next time he used the framework.
        One more benefit of having validateMockitoUsage() in @After is that jUnit runner and rule will always fail in the test method with defect
        whereas ordinary 'next-time' validation might fail the next test method.
        But even though JUnit might report next test as red, don't worry about it
        and just click at navigable stack trace element in the exception message to instantly locate the place where you misused mockito.
        Both built-in runner: MockitoJUnitRunner and rule: MockitoRule do validateMockitoUsage() after each test method.
        Bear in mind that usually you don't have to validateMockitoUsage()
        and framework validation triggered on next-time basis should be just enough,
        mainly because of enhanced exception message with clickable location of defect.
        However, I would recommend validateMockitoUsage() if you already have sufficient test infrastructure
        (like your own runner or base class for all tests) because adding a special action to @After has zero cost.
        See examples in javadoc for Mockito class

# File: `VerificationWithTimeout.java`

## Method: `public VerificationMode atLeast(int minNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atLeast(int minNumberOfInvocations)", "entityFile": "VerificationWithTimeout.java"} --><!-- 77fc6a36-1784-11ea-89bb-333445793454 <=< ACCEPT -->Allows at-least-x verification within given timeout. E.g:
        <pre class="code"><code class="java">
        verify(mock, timeout(100).atLeast(3)).someMethod("some arg");
        See examples in javadoc for Mockito class
        @param minNumberOfInvocations minimum number of invocations
        @return verification mode<!-- ACCEPT >=> 77fc6a36-1784-11ea-89bb-333445793454 -->

# File: `PropertyAndSetterInjection.java`

## Class: `PropertyAndSetterInjection`

        <!-- META {"entityType": "Class", "entitySignature": "PropertyAndSetterInjection", "entityFile": "PropertyAndSetterInjection.java"} -->Inject mocks using first setters then fields, if no setters available.
        Algorithm :
        for each field annotated by @InjectMocks
        initialize field annotated by @InjectMocks
        for each fields of a class in @InjectMocks type hierarchy
        make a copy of mock candidates
        order fields from sub-type to super-type, then by field name
        for the list of fields in a class try two passes of :
        find mock candidate by type
        if more than *one* candidate find mock candidate on name
        if one mock candidate then
        set mock by property setter if possible
        else set mock by field injection
        remove mock from mocks copy (mocks are just injected once in a class)
        remove injected field from list of class fields
        else don't fail, user will then provide dependencies
        Note: If the field needing injection is not initialized, the strategy tries
        to create one using a no-arg constructor of the field type.

# File: `VerificationWithTimeout.java`

## Method: `public VerificationMode atMost(int maxNumberOfInvocations)`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode atMost(int maxNumberOfInvocations)", "entityFile": "VerificationWithTimeout.java"} --><!-- c2fdafe2-1784-11ea-806e-333445793454 <=< ACCEPT -->@deprecated
        Deprecated
        Validation with timeout combined with never simply does not make sense, as atMost() will typically immediately pass,
        and therefore not wait the timeout. The behaviour you may be looking for is actually provided by after().atMost().
        To avoid compilation errors upon upgrade the method is deprecated and it throws a "friendly reminder" exception.
        In a future release we will remove timeout(x).atMost(y) and timeout(x).never() from the API.
        Do you want to find out more? See <a href="http://code.google.com/p/mockito/issues/detail?id=235">issue 235
        @return verification mode<!-- ACCEPT >=> c2fdafe2-1784-11ea-806e-333445793454 -->

## Method: `public VerificationMode only()`

        <!-- META {"entityType": "Method", "entitySignature": "public VerificationMode only()", "entityFile": "VerificationWithTimeout.java"} --><!-- 0078b26c-1785-11ea-a13e-333445793454 <=< ACCEPT -->Allows checking if given method was the only one invoked. E.g:
        <pre class="code"><code class="java">
        verify(mock, only()).someMethod();
        //above is a shorthand for following 2 lines of code:
        verify(mock).someMethod();
        verifyNoMoreInvocations(mock);
        See also Mockito#verifyNoMoreInteractions(Object...)
        See examples in javadoc for Mockito class
        @return verification mode<!-- ACCEPT >=> 0078b26c-1785-11ea-a13e-333445793454 -->

# File: `InjectMocksScanner.java`

## Method: `public InjectMocksScanner(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public InjectMocksScanner(Class<?> clazz)", "entityFile": "InjectMocksScanner.java"} -->Create a new InjectMocksScanner for the given clazz on the given instance
        @param clazz    Current class in the hierarchy of the test

## Method: `public void addTo(Set<Field> mockDependentFields)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addTo(Set<Field> mockDependentFields)", "entityFile": "InjectMocksScanner.java"} -->Add the fields annotated by @InjectMocks
        @param mockDependentFields Set of fields annotated by  @InjectMocks

## Method: `private Set<Field> scan()`

        <!-- META {"entityType": "Method", "entitySignature": "private Set<Field> scan()", "entityFile": "InjectMocksScanner.java"} -->Scan fields annotated by @InjectMocks
        @return Fields that depends on Mock

# File: `Mockito.java`

## Method: `public static MockSettings withSettings()`

        <!-- META {"entityType": "Method", "entitySignature": "public static MockSettings withSettings()", "entityFile": "Mockito.java"} --><!-- 3b872434-1785-11ea-b96e-333445793454 <=< ACCEPT -->Allows mock creation with additional mock settings.
        Don't use it too often.
        Consider writing simple tests that use simple mocks.
        Repeat after me: simple tests push simple, KISSy, readable & maintainable code.
        If you cannot write a test in a simple way - refactor the code under test.
        Examples of mock settings:
        <pre class="code"><code class="java">
        //Creates mock with different default answer & name
        Foo mock = mock(Foo.class, withSettings()
        .defaultAnswer(RETURNS_SMART_NULLS)
        .name("cool mockie"));
        //Creates mock with different default answer, descriptive name and extra interfaces
        Foo mock = mock(Foo.class, withSettings()
        .defaultAnswer(RETURNS_SMART_NULLS)
        .name("cool mockie")
        .extraInterfaces(Bar.class));
        MockSettings has been introduced for two reasons.
        Firstly, to make it easy to add another mock settings when the demand comes.
        Secondly, to enable combining different mock settings without introducing zillions of overloaded mock() methods.
        See javadoc for MockSettings to learn about possible mock settings.
        @return mock settings instance with defaults.<!-- ACCEPT >=> 3b872434-1785-11ea-b96e-333445793454 -->

# File: `VerificationWithTimeout.java`

## Interface: `VerificationWithTimeout`

        <!-- META {"entityType": "Interface", "entitySignature": "VerificationWithTimeout", "entityFile": "VerificationWithTimeout.java"} -->VerificationWithTimeout is a VerificationMode that allows combining existing verification modes with 'timeout'. E.g:
        <pre class="code"><code class="java">
        verify(mock, timeout(100).times(5)).foo();
        verify(mock, timeout(100).never()).bar();
        verify(mock, timeout(200).atLeastOnce()).baz();
        This is similar to VerificationAfterDelay after() except this assertion will immediately pass if it becomes true at any point,
        whereas after() will wait the full period. Assertions which are consistently expected to be initially true and potentially become false
        are deprecated below, and after() should be used instead.
        See examples in javadoc for Mockito#verify(Object, VerificationMode)

# File: `Mockito.java`

## Method: `public static VerificationMode description(String description)`

        <!-- META {"entityType": "Method", "entitySignature": "public static VerificationMode description(String description)", "entityFile": "Mockito.java"} -->Adds a description to be printed if verification fails.
        <pre class="code"><code class="java">
        verify(mock, description("This will print on failure")).someMethod("some arg");
        @param description The description to print on failure.
        @return verification mode
        @since 2.0.0

## Method: `static MockitoDebugger debug()`

        <!-- META {"entityType": "Method", "entitySignature": "static MockitoDebugger debug()", "entityFile": "Mockito.java"} -->Helps debugging failing tests. Experimental - use at your own risk. We're not sure if this method will stay in public api.

# File: `MockScanner.java`

## Method: `public MockScanner(Object instance, Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public MockScanner(Object instance, Class<?> clazz)", "entityFile": "MockScanner.java"} -->Creates a MockScanner.
        @param instance The test instance
        @param clazz    The class in the type hierarchy of this instance.

## Method: `public void addPreparedMocks(Set<Object> mocks)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addPreparedMocks(Set<Object> mocks)", "entityFile": "MockScanner.java"} -->Add the scanned and prepared mock instance to the given collection.
        The preparation of mocks consists only in defining a MockName if not already set.
        @param mocks Set of mocks

## Method: `private Set<Object> scan()`

        <!-- META {"entityType": "Method", "entitySignature": "private Set<Object> scan()", "entityFile": "MockScanner.java"} -->Scan and prepare mocks for the given testClassInstance and clazz in the type hierarchy.
        @return A prepared set of mock

# File: `SpyOnInjectedFieldsHandler.java`

## Class: `SpyOnInjectedFieldsHandler`

        <!-- META {"entityType": "Class", "entitySignature": "SpyOnInjectedFieldsHandler", "entityFile": "SpyOnInjectedFieldsHandler.java"} -->Handler for field annotated with &#64;InjectMocks and &#64;Spy.
        The handler assumes that field initialization AND injection already happened.
        So if the field is still null, then nothing will happen there.

# File: `MockAnnotationProcessor.java`

## Class: `MockAnnotationProcessor`

        <!-- META {"entityType": "Class", "entitySignature": "MockAnnotationProcessor", "entityFile": "MockAnnotationProcessor.java"} -->Instantiates a mock on a field annotated by Mock

# File: `MockitoAnnotationsMockAnnotationProcessor.java`

## Class: `MockitoAnnotationsMockAnnotationProcessor`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoAnnotationsMockAnnotationProcessor", "entityFile": "MockitoAnnotationsMockAnnotationProcessor.java"} -->Instantiates a mock on a field annotated by Mock

# File: `Pluralizer.java`

## Class: `Pluralizer`

        <!-- META {"entityType": "Class", "entitySignature": "Pluralizer", "entityFile": "Pluralizer.java"} -->@Deprecated. This class has been moved to internal packages because it was never meant to be public.
        If you need it for extending Mockito please let us know. You can still use org.mockito.internal.reporting.Pluralizer.
        However, the package clearly states that the class in a part of a public API so it can change.

# File: `PrintableInvocation.java`

## Interface: `PrintableInvocation`

        <!-- META {"entityType": "Interface", "entitySignature": "PrintableInvocation", "entityFile": "PrintableInvocation.java"} -->@Deprecated. We needed to move this class to a better place to keep consistency of the API.
        Please use DescribedInvocation instead.

# File: `PluginLoader.java`

## Method: `T loadPlugin(Class<T> pluginType, String defaultPluginClassName)`

        <!-- META {"entityType": "Method", "entitySignature": "T loadPlugin(Class<T> pluginType, String defaultPluginClassName)", "entityFile": "PluginLoader.java"} -->Scans the classpath for given pluginType. If not found, default class is used.

## Method: `T loadImpl(Class<T> service)`

        <!-- META {"entityType": "Method", "entitySignature": "T loadImpl(Class<T> service)", "entityFile": "PluginLoader.java"} -->Equivalent to java.util.ServiceLoader#load but without requiring
        Java 6 / Android 2.3 (Gingerbread).

# File: `PluginRegistry.java`

## Method: `MockMaker getMockMaker()`

        <!-- META {"entityType": "Method", "entitySignature": "MockMaker getMockMaker()", "entityFile": "PluginRegistry.java"} -->Returns the implementation of the mock maker available for the current runtime.
        Returns org.mockito.internal.creation.cglib.CglibMockMaker if no
        org.mockito.plugins.MockMaker extension exists or is visible in the current classpath.

## Method: `InstantiatorProvider getInstantiatorProvider()`

        <!-- META {"entityType": "Method", "entitySignature": "InstantiatorProvider getInstantiatorProvider()", "entityFile": "PluginRegistry.java"} -->Returns the instantiator provider available for the current runtime.
        Returns org.mockito.internal.creation.instance.DefaultInstantiatorProvider if no
        org.mockito.plugins.InstantiatorProvider extension exists or is visible in the current classpath.

# File: `Plugins.java`

## Method: `public static MockMaker getMockMaker()`

        <!-- META {"entityType": "Method", "entitySignature": "public static MockMaker getMockMaker()", "entityFile": "Plugins.java"} -->Returns the implementation of the mock maker available for the current runtime.
        Returns default mock maker if no
        org.mockito.plugins.MockMaker extension exists or is visible in the current classpath.

## Method: `public static InstantiatorProvider getInstantiatorProvider()`

        <!-- META {"entityType": "Method", "entitySignature": "public static InstantiatorProvider getInstantiatorProvider()", "entityFile": "Plugins.java"} -->Returns the instantiator provider available for the current runtime.
        Returns org.mockito.internal.creation.instance.DefaultInstantiatorProvider if no
        org.mockito.plugins.InstantiatorProvider extension exists or is visible in the current classpath.

## Class: `Plugins`

        <!-- META {"entityType": "Class", "entitySignature": "Plugins", "entityFile": "Plugins.java"} -->Access to Mockito behavior that can be reconfigured by plugins

# File: `SpyAnnotationEngine.java`

## Class: `SpyAnnotationEngine`

        <!-- META {"entityType": "Class", "entitySignature": "SpyAnnotationEngine", "entityFile": "SpyAnnotationEngine.java"} -->Process fields annotated with &#64;Spy.
        Will try transform the field in a spy as with Mockito.spy().
        If the field is not initialized, will try to initialize it, with a no-arg constructor.
        If the field is also annotated with the compatible &#64;InjectMocks then the field will be ignored,
        The injection engine will handle this specific case.
        This engine will fail, if the field is also annotated with incompatible Mockito annotations.

# File: `Reporter.java`

## Class: `Reporter`

        <!-- META {"entityType": "Class", "entitySignature": "Reporter", "entityFile": "Reporter.java"} -->Reports verification and misusing errors.
        One of the key points of mocking library is proper verification/exception
        messages. All messages in one place makes it easier to tune and amend them.
        Reporter can be injected and therefore is easily testable.
        Generally, exception messages are full of line breaks to make them easy to
        read (xunit plugins take only fraction of screen on modern IDEs).

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Method: `public Object writeReplace(Object mockitoMock) throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "public Object writeReplace(Object mockitoMock) throws ObjectStreamException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Custom implementation of the writeReplace method for serialization.
        Here's how it's working and why :
        When first entering in this method, it's because some is serializing the mock, with some code like :
        <pre class="code"><code class="java">
        objectOutputStream.writeObject(mock);
        So, ObjectOutputStream will track the writeReplace method in the instance and
        execute it, which is wanted to replace the mock by another type that will encapsulate the actual mock.
        At this point, the code will return an
        CrossClassLoaderSerializableMock.
        Now, in the constructor
        CrossClassLoaderSerializationProxy#CrossClassLoaderSerializationProxy(java.lang.Object)
        the mock is being serialized in a custom way (using MockitoMockObjectOutputStream) to a
        byte array. So basically it means the code is performing double nested serialization of the passed
        mockitoMock.
        However the ObjectOutputStream will still detect the custom
        writeReplace and execute it.
        (For that matter disabling replacement via ObjectOutputStream#enableReplaceObject(boolean)
        doesn't disable the writeReplace call, but just just toggle replacement in the
        written stream, writeReplace is always called by
        ObjectOutputStream.)
        In order to avoid this recursion, obviously leading to a StackOverflowError, this method is using
        a flag that marks the mock as already being replaced, and then shouldn't replace itself again.
        This flag is local to this class, which means the flag of this class unfortunately needs
        to be protected against concurrent access, hence the reentrant lock.
        @param mockitoMock The Mockito mock to be serialized.
        @return A wrapper (CrossClassLoaderSerializationProxy) to be serialized by the calling ObjectOutputStream.
        @throws java.io.ObjectStreamException

# File: `StackTraceCleaner.java`

## Method: `boolean isOut(StackTraceElement candidate)`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isOut(StackTraceElement candidate)", "entityFile": "StackTraceCleaner.java"} -->Decides if element is excluded.
        @param candidate element of the actual stack trace
        @return whether the element should be excluded from cleaned stack trace.

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Method: `public CrossClassLoaderSerializationProxy(Object mockitoMock) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public CrossClassLoaderSerializationProxy(Object mockitoMock) throws IOException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Creates the wrapper that be used in the serialization stream.
        Immediately serializes the Mockito mock using specifically crafted MockitoMockObjectOutputStream,
        in a byte array.
        @param mockitoMock The Mockito mock to serialize.
        @throws java.io.IOException

## Method: `private Object readResolve() throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "private Object readResolve() throws ObjectStreamException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Resolves the proxy to a new deserialized instance of the Mockito mock.
        Uses the custom crafted MockitoMockObjectInputStream to deserialize the mock.
        @return A deserialized instance of the Mockito mock.
        @throws java.io.ObjectStreamException

# File: `StackTraceCleaner.java`

## Interface: `StackTraceCleaner`

        <!-- META {"entityType": "Interface", "entitySignature": "StackTraceCleaner", "entityFile": "StackTraceCleaner.java"} -->Decides if particular StackTraceElement is excluded from the human-readable stack trace output.
        Mockito stack trace filtering mechanism uses this information.
        Excluding an element will make it not show in the cleaned stack trace.
        Not-excluding an element does not guarantee it will be shown
        (e.g. it depends on the implementation of
        Mockito internal org.mockito.internal.exceptions.stacktrace.StackTraceFilter).
        The implementations are required to be thread safe. For example, make them stateless.
        See the default implementation: org.mockito.internal.exceptions.stacktrace.DefaultStackTraceCleaner.

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Class: `CrossClassLoaderSerializationProxy`

        <!-- META {"entityType": "Class", "entitySignature": "CrossClassLoaderSerializationProxy", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->This is the serialization proxy that will encapsulate the real mock data as a byte array.
        When called in the constructor it will serialize the mock in a byte array using a
        custom MockitoMockObjectOutputStream that will annotate the mock class in the stream.
        Other information are used in this class in order to facilitate deserialization.
        Deserialization of the mock will be performed by the #readResolve() method via
        the custom MockitoMockObjectInputStream that will be in charge of creating the mock class.

## Method: `protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException, ClassNotFoundException`

        <!-- META {"entityType": "Method", "entitySignature": "protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException, ClassNotFoundException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Resolve the Mockito proxy class if it is marked as such.
        Uses the fields #typeToMock and #extraInterfaces to
        create the Mockito proxy class as the ObjectStreamClass
        doesn't carry useful information for this purpose.
        @param desc Description of the class in the stream, not used.
        @return The class that will be used to deserialize the instance mock.
        @throws java.io.IOException
        @throws ClassNotFoundException

## Method: `private void hackClassNameToMatchNewlyCreatedClass(ObjectStreamClass descInstance, Class<?> proxyClass) throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "private void hackClassNameToMatchNewlyCreatedClass(ObjectStreamClass descInstance, Class<?> proxyClass) throws ObjectStreamException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Hack the name field of the given ObjectStreamClass with
        the newProxyClass.
        The parent ObjectInputStream will check the name of the class in the stream matches the name of the one
        that is created in this method.
        The CGLIB classes uses a hash of the classloader and/or maybe some other data that allow them to be
        relatively unique in a JVM.
        When names differ, which happens when the mock is deserialized in another ClassLoader, a
        java.io.InvalidObjectException is thrown, so this part of the code is hacking through
        the given ObjectStreamClass to change the name with the newly created class.
        @param descInstance The ObjectStreamClass that will be hacked.
        @param proxyClass   The proxy class whose name will be applied.
        @throws java.io.InvalidObjectException

# File: `JUnitTool.java`

## Class: `JUnitTool`

        <!-- META {"entityType": "Class", "entitySignature": "JUnitTool", "entityFile": "JUnitTool.java"} -->@Deprecated. This class has been moved to internal packages because it was never meant to be public.
        If you need it for extending Mockito please let us know. You can still use org.mockito.internal.junit.JUnitTool.
        However, the package clearly states that the class in a part of a public API so it can change.

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Method: `private boolean notMarkedAsAMockitoMock(Object marker) throws IOException, ClassNotFoundException`

        <!-- META {"entityType": "Method", "entitySignature": "private boolean notMarkedAsAMockitoMock(Object marker) throws IOException, ClassNotFoundException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Read the stream class annotation and identify it as a Mockito mock or not.
        @param marker The marker to identify.
        @return true if not marked as a Mockito, false if the class annotation marks a Mockito mock.
        @throws java.io.IOException
        @throws ClassNotFoundException

# File: `NoInteractionsWanted.java`

## Class: `NoInteractionsWanted`

        <!-- META {"entityType": "Class", "entitySignature": "NoInteractionsWanted", "entityFile": "NoInteractionsWanted.java"} -->No interactions wanted. See exception's cause for location of undesired invocation.

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Class: `MockitoMockObjectInputStream`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoMockObjectInputStream", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Special Mockito aware ObjectInputStream that will resolve the Mockito proxy class.
        This specifically crafted ObjectInoutStream has the most important role to resolve the Mockito generated
        class. It is doing so via the #resolveClass(ObjectStreamClass) which looks in the stream
        for a Mockito marker. If this marker is found it will try to resolve the mockito class otherwise it
        delegates class resolution to the default super behavior.
        The mirror method used for serializing the mock is MockitoMockObjectOutputStream#annotateClass(Class).
        When this marker is found, ByteBuddyMockMaker#createProxyClass(MockFeatures) methods are being used
        to create the mock class.

## Method: `protected void annotateClass(Class<?> cl) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "protected void annotateClass(Class<?> cl) throws IOException", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Annotates (marks) the class if this class is a Mockito mock.
        @param cl The class to annotate.
        @throws java.io.IOException

## Method: `private String mockitoProxyClassMarker(Class<?> cl)`

        <!-- META {"entityType": "Method", "entitySignature": "private String mockitoProxyClassMarker(Class<?> cl)", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Returns the Mockito marker if this class is a Mockito mock.
        @param cl The class to mark.
        @return The marker if this is a Mockito proxy class, otherwise returns a void marker.

## Class: `MockitoMockObjectOutputStream`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoMockObjectOutputStream", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Special Mockito aware ObjectOutputStream.
        This output stream has the role of marking in the stream the Mockito class. This
        marking process is necessary to identify the proxy class that will need to be recreated.
        The mirror method used for deserializing the mock is
        MockitoMockObjectInputStream#resolveClass(ObjectStreamClass).

## Interface: `CrossClassLoaderSerializableMock`

        <!-- META {"entityType": "Interface", "entitySignature": "CrossClassLoaderSerializableMock", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->Simple interface that hold a correct writeReplace signature that can be seen by an
        ObjectOutputStream.
        It will be applied before the creation of the mock when the mock setting says it should serializable.

# File: `MockitoHamcrest.java`

## Method: `public static T argThat(Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T argThat(Matcher<T> matcher)", "entityFile": "MockitoHamcrest.java"} -->Allows matching arguments with hamcrest matchers.
        See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return null or default value for primitive (0, false, etc.)
        @since 2.0

## Method: `public static char charThat(Matcher<Character> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char charThat(Matcher<Character> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive char arguments.
        Note that #argThat will not work with primitive char matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

# File: `ByteBuddyCrossClassLoaderSerializationSupport.java`

## Class: `ByteBuddyCrossClassLoaderSerializationSupport`

        <!-- META {"entityType": "Class", "entitySignature": "ByteBuddyCrossClassLoaderSerializationSupport", "entityFile": "ByteBuddyCrossClassLoaderSerializationSupport.java"} -->This is responsible for serializing a mock, it is enabled if the mock is implementing Serializable.
        The way it works is to enable serialization via the flag MockFeatures#crossClassLoaderSerializable,
        if the mock settings is set to be serializable the mock engine will implement the
        CrossClassLoaderSerializableMock marker interface.
        This interface defines a the CrossClassLoaderSerializableMock#writeReplace()
        whose signature match the one that is looked by the standard Java serialization.
        Then in the proxy class there will be a generated writeReplace that will delegate to
        ForWriteReplace#doWriteReplace(MockAccess) of mockito, and in turn will delegate to the custom
        implementation of this class #writeReplace(Object). This method has a specific
        knowledge on how to serialize a mockito mock that is based on ByteBuddy and will ignore other Mockito MockMakers.
        Only one instance per mock! See MockMethodInterceptor
        TODO check the class is mockable in the deserialization side
        @see org.mockito.internal.creation.bytebuddy.ByteBuddyMockMaker
        @see org.mockito.internal.creation.bytebuddy.MockMethodInterceptor
        @author Brice Dutheil
        @since 1.10.0

# File: `MockitoHamcrest.java`

## Method: `public static boolean booleanThat(Matcher<Boolean> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean booleanThat(Matcher<Boolean> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive boolean arguments.
        Note that #argThat will not work with primitive boolean matchers due to NullPointerException auto-unboxing caveat.
        See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return false.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static byte byteThat(Matcher<Byte> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte byteThat(Matcher<Byte> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive byte arguments.
        Note that #argThat will not work with primitive byte matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static short shortThat(Matcher<Short> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short shortThat(Matcher<Short> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive short arguments.
        Note that #argThat will not work with primitive short matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static int intThat(Matcher<Integer> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int intThat(Matcher<Integer> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive int arguments.
        Note that #argThat will not work with primitive int matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static long longThat(Matcher<Long> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long longThat(Matcher<Long> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive long arguments.
        Note that #argThat will not work with primitive long matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static float floatThat(Matcher<Float> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float floatThat(Matcher<Float> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive float arguments.
        Note that #argThat will not work with primitive float matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Method: `public static double doubleThat(Matcher<Double> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double doubleThat(Matcher<Double> matcher)", "entityFile": "MockitoHamcrest.java"} --><!-- f9ffd5ae-1781-11ea-986d-333445793454 <=< ACCEPT -->Enables integrating hamcrest matchers that match primitive double arguments.
        Note that #argThat will not work with primitive double matchers due to NullPointerException auto-unboxing caveat.
        * See examples in javadoc for MockitoHamcrest class
        @param matcher decides whether argument matches
        @return 0.<!-- ACCEPT >=> f9ffd5ae-1781-11ea-986d-333445793454 -->

## Class: `MockitoHamcrest`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoHamcrest", "entityFile": "MockitoHamcrest.java"} -->Allows matching arguments with hamcrest matchers.
        Requires <a href="http://hamcrest.org/JavaHamcrest/">hamcrest on classpath,
        Mockito does not depend on hamcrest!
        Note the NullPointerException auto-unboxing caveat described below.
        Before implementing or reusing an existing hamcrest matcher please read
        how to deal with sophisticated argument matching in ArgumentMatcher.
        Mockito 2.0 was decoupled from Hamcrest to avoid version incompatibilities
        that have impacted our users in past. Mockito offers a dedicated API to match arguments
        via ArgumentMatcher.
        Hamcrest integration is provided so that users can take advantage of existing Hamcrest matchers.
        Example:
        import static org.mockito.hamcrest.MockitoHamcrest.argThat;
        //stubbing
        when(mock.giveMe(argThat(new MyHamcrestMatcher())));
        //verification
        verify(mock).giveMe(argThat(new MyHamcrestMatcher()));
        NullPointerException auto-unboxing caveat.
        In rare cases when matching primitive parameter types you *must* use relevant intThat(), floatThat(), etc. method.
        This way you will avoid NullPointerException during auto-unboxing.
        Due to how java works we don't really have a clean way of detecting this scenario and protecting the user from this problem.
        Hopefully, the javadoc describes the problem and solution well.
        If you have an idea how to fix the problem, let us know via the mailing list or the issue tracker.
        @since 2.0

# File: `Incubating.java`

## Annotation: `Incubating`

        <!-- META {"entityType": "Annotation", "entitySignature": "Incubating", "entityFile": "Incubating.java"} -->The annotation conveys following information:
        The API is fairly new and we would appreciate your feedback. For example, what are you missing from the API
        to solve your use case.
        The API might change.
        The chance for that is small because we care great deal for the initial design.
        The incubating API might change based on the feedback from the community in order to make the API most useful for the users.
        For types or methods that are not yet released it means the API is work in progress
        and can change before release.

# File: `DelegatingMethod.java`

## Method: `public boolean equals(Object o)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean equals(Object o)", "entityFile": "DelegatingMethod.java"} -->@return True if the input object is a DelegatingMethod which has an internal Method which is equal to the internal Method of this DelegatingMethod,
        or if the input object is a Method which is equal to the internal Method of this DelegatingMethod.

# File: `InjectMocks.java`

## Annotation: `InjectMocks`

        <!-- META {"entityType": "Annotation", "entitySignature": "InjectMocks", "entityFile": "InjectMocks.java"} -->Mark a field on which injection should be performed.
        Allows shorthand mock and spy injection.
        Minimizes repetitive mock and spy injection.
        Mockito will try to inject mocks only either by constructor injection,
        setter injection, or property injection in order and as described below.
        If any of the following strategy fail, then Mockito won't report failure;
        i.e. you will have to provide dependencies yourself.
        Constructor injection; the biggest constructor is chosen,
        then arguments are resolved with mocks declared in the test only. If the object is successfully created
        with the constructor, then Mockito won't try the other strategies. Mockito has decided to no
        corrupt an object if it has a parametered constructor.
        Note: If arguments can not be found, then null is passed.
        If non-mockable types are wanted, then constructor injection won't happen.
        In these cases, you will have to satisfy dependencies yourself.
        Property setter injection; mocks will first be resolved by type (if a single type match
        injection will happen regardless of the name),
        then, if there is several property of the same type, by the match of the property name and the mock name.
        Note 1: If you have properties with the same type (or same erasure), it's better to name all @Mock
        annotated fields with the matching properties, otherwise Mockito might get confused and injection won't happen.
        Note 2: If @InjectMocks instance wasn't initialized before and have a no-arg constructor,
        then it will be initialized with this constructor.
        Field injection; mocks will first be resolved by type (if a single type match
        injection will happen regardless of the name),
        then, if there is several property of the same type, by the match of the field name and the mock name.
        Note 1: If you have fields with the same type (or same erasure), it's better to name all @Mock
        annotated fields with the matching fields, otherwise Mockito might get confused and injection won't happen.
        Note 2: If @InjectMocks instance wasn't initialized before and have a no-arg constructor,
        then it will be initialized with this constructor.
        Example:
        <pre class="code"><code class="java">
        public class ArticleManagerTest extends SampleBaseTestCase {
        @Mock private ArticleCalculator calculator;
        @Mock(name = "database") private ArticleDatabase dbMock; // note the mock name attribute
        @Spy private UserProvider userProvider = new ConsumerUserProvider();
        @InjectMocks private ArticleManager manager;
        @Test public void shouldDoSomething() {
        manager.initiateArticle();
        verify(database).addListener(any(ArticleListener.class));
        }
        }
        public class SampleBaseTestCase {
        @Before public void initMocks() {
        MockitoAnnotations.initMocks(this);
        }
        }
        In the above example the field ArticleManager annotated with @InjectMocks can have
        a parameterized constructor only or a no-arg constructor only, or both.
        All these constructors can be package protected, protected or private, however
        Mockito cannot instantiate inner classes, local classes, abstract classes and of course interfaces.
        Beware of private nest static classes too.
        The same stands for setters or fields, they can be declared with private
        visibility, Mockito will see them through reflection.
        However fields that are static or final will be ignored.
        So on the field that needs injection, for example constructor injection will happen here :
        <pre class="code"><code class="java">
        public class ArticleManager {
        ArticleManager(ArticleCalculator calculator, ArticleDatabase database) {
        // parameterized constructor
        }
        }
        Property setter injection will happen here :
        <pre class="code"><code class="java">
        public class ArticleManager {
        // no-arg constructor
        ArticleManager() {  }
        // setter
        void setDatabase(ArticleDatabase database) { }
        // setter
        void setCalculator(ArticleCalculator calculator) { }
        }
        Field injection will be used here :
        <pre class="code"><code class="java">
        public class ArticleManager {
        private ArticleDatabase database;
        private ArticleCalculator calculator;
        }
        And finally, no injection will happen on the type in this case:
        <pre class="code"><code class="java">
        public class ArticleManager {
        private ArticleDatabase database;
        private ArticleCalculator calculator;
        ArticleManager(ArticleObserver observer, boolean flag) {
        // observer is not declared in the test above.
        // flag is not mockable anyway
        }
        }
        Again, note that @InjectMocks will only inject mocks/spies created using the &#64;Spy or &#64;Mock annotation.
        MockitoAnnotations.initMocks(this) method has to be called to initialize annotated objects.
        In above example, initMocks() is called in @Before (JUnit4) method of test's base class.
        For JUnit3 initMocks() can go to setup() method of a base class.
        Instead you can also put initMocks() in your JUnit runner (@RunWith) or use the built-in
        org.mockito.runners.MockitoJUnitRunner.
        Mockito is not an dependency injection framework, don't expect this shorthand utility to inject a complex graph of objects
        be it mocks/spies or real objects.
        @see Mock
        @see Spy
        @see MockitoAnnotations#initMocks(Object)
        @see org.mockito.runners.MockitoJUnitRunner
        @since 1.8.3

# File: `AdditionalAnswers.java`

## Method: `public static Answer<T> returnsFirstArg()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> returnsFirstArg()", "entityFile": "AdditionalAnswers.java"} -->Returns the first parameter of an invocation.
        This additional answer could be used at stub time using the
        then|do|willorg.mockito.stubbing.Answer methods. For example :
        <pre class="code"><code class="java">given(carKeyFob.authenticate(carKey)).will(returnsFirstArg());
        doAnswer(returnsFirstArg()).when(carKeyFob).authenticate(carKey)
        @param <T> Return type of the invocation.
        @return Answer that will return the first argument of the invocation.
        @since 1.9.5

## Method: `public static Answer<T> returnsSecondArg()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> returnsSecondArg()", "entityFile": "AdditionalAnswers.java"} -->Returns the second parameter of an invocation.
        This additional answer could be used at stub time using the
        then|do|willorg.mockito.stubbing.Answer methods. For example :
        <pre class="code"><code class="java">given(trader.apply(leesFormula, onCreditDefaultSwap)).will(returnsSecondArg());
        doAnswer(returnsSecondArg()).when(trader).apply(leesFormula, onCreditDefaultSwap)
        @param <T> Return type of the invocation.
        @return Answer that will return the second argument of the invocation.
        @since 1.9.5

## Method: `public static Answer<T> returnsLastArg()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> returnsLastArg()", "entityFile": "AdditionalAnswers.java"} --><!-- 9a6e48e8-1785-11ea-9315-333445793454 <=< ACCEPT -->Returns the last parameter of an invocation.
        This additional answer could be used at stub time using the
        then|do|willorg.mockito.stubbing.Answer methods. For example :
        <pre class="code"><code class="java">given(person.remember(dream1, dream2, dream3, dream4)).will(returnsLastArg());
        doAnswer(returnsLastArg()).when(person).remember(dream1, dream2, dream3, dream4)
        @param <T> Return type of the invocation.
        @return Answer that will return the last argument of the invocation.
        @since 1.9.5<!-- ACCEPT >=> 9a6e48e8-1785-11ea-9315-333445793454 -->

## Method: `public static Answer<T> returnsArgAt(int position)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> returnsArgAt(int position)", "entityFile": "AdditionalAnswers.java"} --><!-- 9a6e48e8-1785-11ea-9315-333445793454 <=< ACCEPT -->Returns the parameter of an invocation at the given position.
        This additional answer could be used at stub time using the
        then|do|willorg.mockito.stubbing.Answer methods. For example :
        <pre class="code"><code class="java">given(person.remember(dream1, dream2, dream3, dream4)).will(returnsArgAt(3));
        doAnswer(returnsArgAt(3)).when(person).remember(dream1, dream2, dream3, dream4)
        @param <T> Return type of the invocation.
        @param position index of the argument from the list of arguments.
        @return Answer that will return the argument from the given position in the argument's list
        @since 1.9.5<!-- ACCEPT >=> 9a6e48e8-1785-11ea-9315-333445793454 -->

## Method: `public static Answer<T> delegatesTo(Object delegate)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> delegatesTo(Object delegate)", "entityFile": "AdditionalAnswers.java"} -->An answer that directly forwards the calls to the delegate. The delegate may or may not be of the same type as the mock.
        If the type is different, a matching method needs to be found on delegate type otherwise an exception is thrown.
        Useful for spies or partial mocks of objects that are difficult to mock
        or spy using the usual spy API. Possible use cases:
        Final classes but with an interface
        Already custom proxied object
        Special objects with a finalize method, i.e. to avoid executing it 2 times
        For more details including the use cases reported by users take a look at
        <a link="http://code.google.com/p/mockito/issues/detail?id=145">issue 145.
        The difference with the regular spy:
        The regular spy (Mockito#spy(Object)) contains all state from the spied instance
        and the methods are invoked on the spy. The spied instance is only used at mock creation to copy the state from.
        If you call a method on a regular spy and it internally calls other methods on this spy, those calls are remembered
        for verifications, and they can be effectively stubbed.
        The mock that delegates simply delegates all methods to the delegate.
        The delegate is used all the time as methods are delegated onto it.
        If you call a method on a mock that delegates and it internally calls other methods on this mock,
        those calls are not remembered for verifications, stubbing does not have effect on them, too.
        Mock that delegates is less powerful than the regular spy but it is useful when the regular spy cannot be created.
        An example with a final class that we want to delegate to:
        <pre class="code"><code class="java">
        final class DontYouDareToMockMe implements list { ... }
        DontYouDareToMockMe awesomeList = new DontYouDareToMockMe();
        List mock = mock(List.class, delegatesTo(awesomeList));
        This feature suffers from the same drawback as the spy.
        The mock will call the delegate if you use regular when().then() stubbing style.
        Since the real implementation is called this might have some side effects.
        Therefore you should to use the doReturn|Throw|Answer|CallRealMethod stubbing style. Example:
        <pre class="code"><code class="java">
        List listWithDelegate = mock(List.class, AdditionalAnswers.delegatesTo(awesomeList));
        //Impossible: real method is called so listWithDelegate.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(listWithDelegate.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing
        doReturn("foo").when(listWithDelegate).get(0);
        @param delegate The delegate to forward calls to. It does not have to be of the same type as the mock (although it usually is).
        The only requirement is that the instance should have compatible method signatures including the return values.
        Only the methods that were actually executed on the mock need to be present on the delegate type.
        @return the answer
        @since 1.9.5

## Method: `public static Answer<T> returnsElementsOf(Collection<?> elements)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Answer<T> returnsElementsOf(Collection<?> elements)", "entityFile": "AdditionalAnswers.java"} --><!-- 62e3dc36-1785-11ea-bbed-333445793454 <=< ACCEPT -->Returns elements of the collection. Keeps returning the last element forever.
        Might be useful on occasion when you have a collection of elements to return.
        <pre class="code"><code class="java">
        //this:
        when(mock.foo()).thenReturn(1, 2, 3);
        //is equivalent to:
        when(mock.foo()).thenAnswer(new ReturnsElementsOf(Arrays.asList(1, 2, 3)));
        @param elements The collection of elements to return.
        @return the answer
        @since 1.9.5<!-- ACCEPT >=> 62e3dc36-1785-11ea-bbed-333445793454 -->

## Class: `AdditionalAnswers`

        <!-- META {"entityType": "Class", "entitySignature": "AdditionalAnswers", "entityFile": "AdditionalAnswers.java"} -->Additional answers provides factory methods for less common answers.
        Currently offer answers that can return the parameter of an invocation at a certain position.
        See factory methods for more information : #returnsFirstArg, #returnsSecondArg,
        #returnsLastArg and #returnsArgAt
        @since 1.9.5

# File: `AdditionalMatchers.java`

## Method: `public static T geq(Comparable<T> value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T geq(Comparable<T> value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->argument greater than or equal the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return null.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static byte geq(byte value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte geq(byte value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->byte argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static double geq(double value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double geq(double value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->double argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static float geq(float value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float geq(float value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->float argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static int geq(int value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int geq(int value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->int argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static long geq(long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long geq(long value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->long argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static short geq(short value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short geq(short value)", "entityFile": "AdditionalMatchers.java"} --><!-- c31b849c-1787-11ea-946e-333445793454 <=< ACCEPT -->short argument greater than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> c31b849c-1787-11ea-946e-333445793454 -->

## Method: `public static T leq(Comparable<T> value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T leq(Comparable<T> value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->comparable argument less than or equal the given value details.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return null.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static byte leq(byte value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte leq(byte value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->byte argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static double leq(double value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double leq(double value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->double argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.
        <!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static float leq(float value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float leq(float value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->float argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static int leq(int value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int leq(int value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->int argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static long leq(long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long leq(long value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->long argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static short leq(short value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short leq(short value)", "entityFile": "AdditionalMatchers.java"} --><!-- 815b8a76-1787-11ea-afa9-333445793454 <=< ACCEPT -->short argument less than or equal to the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 815b8a76-1787-11ea-afa9-333445793454 -->

## Method: `public static T gt(Comparable<T> value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T gt(Comparable<T> value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->comparable argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return null.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static byte gt(byte value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte gt(byte value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->byte argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static double gt(double value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double gt(double value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->double argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->.

## Method: `public static float gt(float value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float gt(float value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->float argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static int gt(int value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int gt(int value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->int argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static long gt(long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long gt(long value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->long argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static short gt(short value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short gt(short value)", "entityFile": "AdditionalMatchers.java"} --><!-- 14523c70-1787-11ea-aac4-333445793454 <=< ACCEPT -->short argument greater than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> 14523c70-1787-11ea-aac4-333445793454 -->

## Method: `public static T lt(Comparable<T> value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T lt(Comparable<T> value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->comparable argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return null.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static byte lt(byte value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte lt(byte value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->byte argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static double lt(double value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double lt(double value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->double argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static float lt(float value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float lt(float value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->float argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.
        <!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static int lt(int value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int lt(int value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->int argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static long lt(long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long lt(long value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->long argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static short lt(short value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short lt(short value)", "entityFile": "AdditionalMatchers.java"} --><!-- a2059506-1786-11ea-aa21-333445793454 <=< ACCEPT -->short argument less than the given value.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return 0.<!-- ACCEPT >=> a2059506-1786-11ea-aa21-333445793454 -->

## Method: `public static T cmpEq(Comparable<T> value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T cmpEq(Comparable<T> value)", "entityFile": "AdditionalMatchers.java"} -->comparable argument equals to the given value according to their
        compareTo method.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @return null.

## Method: `public static String find(String regex)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String find(String regex)", "entityFile": "AdditionalMatchers.java"} -->String argument that contains a substring that matches the given regular
        expression.
        @param regex
        the regular expression.
        @return null.

## Method: `public static T[] aryEq(T[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T[] aryEq(T[] value)", "entityFile": "AdditionalMatchers.java"} -->Object array argument that is equal to the given array, i.e. it has to
        have the same type, length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param <T>
        the type of the array, it is passed through to prevent casts.
        @param value
        the given array.
        @return null.

## Method: `public static short[] aryEq(short[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short[] aryEq(short[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->short array argument that is equal to the given array, i.e. it has to
        have the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static long[] aryEq(long[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long[] aryEq(long[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->long array argument that is equal to the given array, i.e. it has to have
        the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static int[] aryEq(int[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int[] aryEq(int[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->int array argument that is equal to the given array, i.e. it has to have
        the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static float[] aryEq(float[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float[] aryEq(float[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->float array argument that is equal to the given array, i.e. it has to
        have the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.
        <!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static double[] aryEq(double[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double[] aryEq(double[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->double array argument that is equal to the given array, i.e. it has to
        have the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.
        <!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static char[] aryEq(char[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char[] aryEq(char[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->char array argument that is equal to the given array, i.e. it has to have
        the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static byte[] aryEq(byte[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte[] aryEq(byte[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->byte array argument that is equal to the given array, i.e. it has to have
        the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static boolean[] aryEq(boolean[] value)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean[] aryEq(boolean[] value)", "entityFile": "AdditionalMatchers.java"} --><!-- cb9c89b4-1785-11ea-8c27-333445793454 <=< ACCEPT -->boolean array argument that is equal to the given array, i.e. it has to
        have the same length, and each element has to be equal.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given array.
        @return null.<!-- ACCEPT >=> cb9c89b4-1785-11ea-8c27-333445793454 -->

## Method: `public static boolean and(boolean first, boolean second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean and(boolean first, boolean second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->boolean argument that matches both given matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return false.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static byte and(byte first, byte second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte and(byte first, byte second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->byte argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static char and(char first, char second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char and(char first, char second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->char argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.
        <!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static double and(double first, double second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double and(double first, double second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->double argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static float and(float first, float second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float and(float first, float second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->float argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static int and(int first, int second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int and(int first, int second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->int argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static long and(long first, long second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long and(long first, long second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->long argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static short and(short first, short second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short and(short first, short second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->short argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.
        <!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static T and(T first, T second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T and(T first, T second)", "entityFile": "AdditionalMatchers.java"} -->Object argument that matches both given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param <T>
        the type of the object, it is passed through to prevent casts.
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return null.

# File: `Mockito.java`

## Class: `Mockito`

        <!-- META {"entityType": "Class", "entitySignature": "Mockito", "entityFile": "Mockito.java"} --><p align="left"><img src="logo.png" srcset="logo@2x.png 2x" alt="Mockito logo"/>
        The Mockito library enables mock creation, verification and stubbing.
        This javadoc content is also available on the <a href="http://mockito.org">http://mockito.org web page.
        All documentation is kept in javadocs because it guarantees consistency between what's on the web and what's in the source code.
        It allows access to documentation straight from the IDE even if you work offline.
        It motivates Mockito developers to keep documentation up-to-date with the code that they write,
        every day, with every commit.
        Contents
        <a href="#0">0. Migrating to 2.0
        <a href="#1">1. Let's verify some behaviour!
        <a href="#2">2. How about some stubbing?
        <a href="#3">3. Argument matchers
        <a href="#4">4. Verifying exact number of invocations / at least once / never
        <a href="#5">5. Stubbing void methods with exceptions
        <a href="#6">6. Verification in order
        <a href="#7">7. Making sure interaction(s) never happened on mock
        <a href="#8">8. Finding redundant invocations
        <a href="#9">9. Shorthand for mocks creation - @Mock annotation
        <a href="#10">10. Stubbing consecutive calls (iterator-style stubbing)
        <a href="#11">11. Stubbing with callbacks
        <a href="#12">12. doReturn()|doThrow()|doAnswer()|doNothing()|doCallRealMethod() family of methods
        <a href="#13">13. Spying on real objects
        <a href="#14">14. Changing default return values of unstubbed invocations (Since 1.7)
        <a href="#15">15. Capturing arguments for further assertions (Since 1.8.0)
        <a href="#16">16. Real partial mocks (Since 1.8.0)
        <a href="#17">17. Resetting mocks (Since 1.8.0)
        <a href="#18">18. Troubleshooting & validating framework usage (Since 1.8.0)
        <a href="#19">19. Aliases for behavior driven development (Since 1.8.0)
        <a href="#20">20. Serializable mocks (Since 1.8.1)
        <a href="#21">21. New annotations: @Captor, @Spy, @InjectMocks (Since 1.8.3)
        <a href="#22">22. Verification with timeout (Since 1.8.5)
        <a href="#23">23. Automatic instantiation of @Spies, @InjectMocks and constructor injection goodness (Since 1.9.0)
        <a href="#24">24. One-liner stubs (Since 1.9.0)
        <a href="#25">25. Verification ignoring stubs (Since 1.9.0)
        <a href="#26">26. Mocking details (Since 1.9.5)
        <a href="#27">27. Delegate calls to real instance (Since 1.9.5)
        <a href="#28">28. MockMaker API (Since 1.9.5)
        <a href="#29">29. (new) BDD style verification (Since 1.10.0)
        <a href="#30">30. (new) Spying or mocking abstract classes (Since 1.10.12)
        <a href="#31">31. (new) Mockito mocks can be serialized / deserialized across classloaders (Since 1.10.0)
        <a href="#32">32. (new) Better generic support with deep stubs (Since 1.10.0)
        <a href="#32">33. (new) Mockito JUnit rule (Since 1.10.17)
        <a href="#34">34. (new) Switch on or off plugins (Since 1.10.15)
        <a href="#35">35. (new) Custom verification failure message (Since 2.0.0)
        <h3 id="0">0. <a class="meaningful_link" href="#verification">Migrating to 2.0
        In order to continue improving Mockito and further improve the unit testing experience, we want you to upgrade to 2.0.
        Mockito follows <a href="http://semver.org/">semantic versioning
        and contains breaking changes only on major version upgrades.
        In the lifecycle of a library, breaking changes are necessary
        to roll out a set of brand new features that alter the existing behavior or even change the API.
        We hope that you enjoy Mockito 2.0!
        List of breaking changes:
        Mockito is decoupled from Hamcrest and custom matchers API has changed, see ArgumentMatcher
        for rationale and migration guide.
        Stubbing API has been tweaked to avoid unavoidable compilation warnings that appeared on JDK7+ platform.
        This will only affect binary compatibility, compilation compatibility remains unaffected.
        The following examples mock a List, because most people are familiar with the interface (such as the
        add(), get(), clear() methods).
        In reality, please don't mock the List class. Use a real instance instead.
        <h3 id="1">1. <a class="meaningful_link" href="#verification">Let's verify some behaviour!
        <pre class="code"><code class="java">
        //Let's import Mockito statically so that the code looks clearer
        import static org.mockito.Mockito.*;
        //mock creation
        List mockedList = mock(List.class);
        //using mock object
        mockedList.add("one");
        mockedList.clear();
        //verification
        verify(mockedList).add("one");
        verify(mockedList).clear();
        Once created, a mock will remember all interactions. Then you can selectively
        verify whatever interactions you are interested in.
        <h3 id="2">2. <a class="meaningful_link" href="#stubbing">How about some stubbing?
        <pre class="code"><code class="java">
        //You can mock concrete classes, not just interfaces
        LinkedList mockedList = mock(LinkedList.class);
        //stubbing
        when(mockedList.get(0)).thenReturn("first");
        when(mockedList.get(1)).thenThrow(new RuntimeException());
        //following prints "first"
        System.out.println(mockedList.get(0));
        //following throws runtime exception
        System.out.println(mockedList.get(1));
        //following prints "null" because get(999) was not stubbed
        System.out.println(mockedList.get(999));
        //Although it is possible to verify a stubbed invocation, usually it's just redundant
        //If your code cares what get(0) returns, then something else breaks (often even before verify() gets executed).
        //If your code doesn't care what get(0) returns, then it should not be stubbed. Not convinced? See <a href="http://monkeyisland.pl/2008/04/26/asking-and-telling">here.
        verify(mockedList).get(0);
        By default, for all methods that return a value, a mock will return either null, a
        a primitive/primitive wrapper value, or an empty collection, as appropriate.
        For example 0 for an int/Integer and false for a boolean/Boolean.
        Stubbing can be overridden: for example common stubbing can go to
        fixture setup but the test methods can override it.
        Please note that overridding stubbing is a potential code smell that points out too much stubbing
        Once stubbed, the method will always return a stubbed value, regardless
        of how many times it is called.
        Last stubbing is more important - when you stubbed the same method with
        the same arguments many times.
        Other words: the order of stubbing matters but it is only meaningful rarely,
        e.g. when stubbing exactly the same method calls or sometimes when argument matchers are used, etc.
        <h3 id="3">3. <a class="meaningful_link" href="#argument_matchers">Argument matchers
        Mockito verifies argument values in natural java style: by using an equals() method.
        Sometimes, when extra flexibility is required then you might use argument matchers:
        <pre class="code"><code class="java">
        //stubbing using built-in anyInt() argument matcher
        when(mockedList.get(anyInt())).thenReturn("element");
        //stubbing using custom matcher (let's say isValid() returns your own matcher implementation):
        when(mockedList.contains(argThat(isValid()))).thenReturn("element");
        //following prints "element"
        System.out.println(mockedList.get(999));
        //you can also verify using an argument matcher
        verify(mockedList).get(anyInt());
        Argument matchers allow flexible verification or stubbing.
        Matchers Click here to see more built-in matchers
        and examples of custom argument matchers / hamcrest matchers.
        For information solely on custom argument matchers check out javadoc for ArgumentMatcher class.
        Be reasonable with using complicated argument matching.
        The natural matching style using equals() with occasional anyX() matchers tend to give clean & simple tests.
        Sometimes it's just better to refactor the code to allow equals() matching or even implement equals() method to help out with testing.
        Also, read <a href="#15">section 15 or javadoc for ArgumentCaptor class.
        ArgumentCaptor is a special implementation of an argument matcher that captures argument values for further assertions.
        Warning on argument matchers:
        If you are using argument matchers, all arguments have to be provided
        by matchers.
        The following example shows verification but the same applies to stubbing:
        <pre class="code"><code class="java">
        verify(mock).someMethod(anyInt(), anyString(), eq("third argument"));
        //above is correct - eq() is also an argument matcher
        verify(mock).someMethod(anyInt(), anyString(), "third argument");
        //above is incorrect - exception will be thrown because third argument is given without an argument matcher.
        Matcher methods like anyObject(), eq() do not return matchers.
        Internally, they record a matcher on a stack and return a dummy value (usually null).
        This implementation is due to static type safety imposed by the java compiler.
        The consequence is that you cannot use anyObject(), eq() methods outside of verified/stubbed method.
        <h3 id="4">4. <a class="meaningful_link" href="#exact_verification">Verifying exact number of invocations /
        <a class="meaningful_link" href="#at_least_verification">at least x / never
        <pre class="code"><code class="java">
        //using mock
        mockedList.add("once");
        mockedList.add("twice");
        mockedList.add("twice");
        mockedList.add("three times");
        mockedList.add("three times");
        mockedList.add("three times");
        //following two verifications work exactly the same - times(1) is used by default
        verify(mockedList).add("once");
        verify(mockedList, times(1)).add("once");
        //exact number of invocations verification
        verify(mockedList, times(2)).add("twice");
        verify(mockedList, times(3)).add("three times");
        //verification using never(). never() is an alias to times(0)
        verify(mockedList, never()).add("never happened");
        //verification using atLeast()/atMost()
        verify(mockedList, atLeastOnce()).add("three times");
        verify(mockedList, atLeast(2)).add("five times");
        verify(mockedList, atMost(5)).add("three times");
        times(1) is the default. Therefore using times(1) explicitly can be
        omitted.
        <h3 id="5">5. <a class="meaningful_link" href="#stubbing_with_exceptions">Stubbing void methods with exceptions
        <pre class="code"><code class="java">
        doThrow(new RuntimeException()).when(mockedList).clear();
        //following throws RuntimeException:
        mockedList.clear();
        Read more about doThrow|doAnswer family of methods in paragraph 12.
        Initially, Mockito#stubVoid(Object) was used for stubbing voids.
        Currently stubVoid() is deprecated in favor of Mockito#doThrow(Throwable...).
        This is because of improved readability and consistency with the family of Mockito#doAnswer(Answer) methods.
        <h3 id="6">6. <a class="meaningful_link" href="#in_order_verification">Verification in order
        <pre class="code"><code class="java">
        // A. Single mock whose methods must be invoked in a particular order
        List singleMock = mock(List.class);
        //using a single mock
        singleMock.add("was added first");
        singleMock.add("was added second");
        //create an inOrder verifier for a single mock
        InOrder inOrder = inOrder(singleMock);
        //following will make sure that add is first called with "was added first, then with "was added second"
        inOrder.verify(singleMock).add("was added first");
        inOrder.verify(singleMock).add("was added second");
        // B. Multiple mocks that must be used in a particular order
        List firstMock = mock(List.class);
        List secondMock = mock(List.class);
        //using mocks
        firstMock.add("was called first");
        secondMock.add("was called second");
        //create inOrder object passing any mocks that need to be verified in order
        InOrder inOrder = inOrder(firstMock, secondMock);
        //following will make sure that firstMock was called before secondMock
        inOrder.verify(firstMock).add("was called first");
        inOrder.verify(secondMock).add("was called second");
        // Oh, and A + B can be mixed together at will
        Verification in order is flexible - you don't have to verify all
        interactions one-by-one but only those that you are interested in
        testing in order.
        Also, you can create an InOrder object passing only the mocks that are relevant for
        in-order verification.
        <h3 id="7">7. <a class="meaningful_link" href="#never_verification">Making sure interaction(s) never happened on mock
        <pre class="code"><code class="java">
        //using mocks - only mockOne is interacted
        mockOne.add("one");
        //ordinary verification
        verify(mockOne).add("one");
        //verify that method was never called on a mock
        verify(mockOne, never()).add("two");
        //verify that other mocks were not interacted
        verifyZeroInteractions(mockTwo, mockThree);
        <h3 id="8">8. <a class="meaningful_link" href="#finding_redundant_invocations">Finding redundant invocations
        <pre class="code"><code class="java">
        //using mocks
        mockedList.add("one");
        mockedList.add("two");
        verify(mockedList).add("one");
        //following verification will fail
        verifyNoMoreInteractions(mockedList);
        A word of warning:
        Some users who did a lot of classic, expect-run-verify mocking tend to use verifyNoMoreInteractions() very often, even in every test method.
        verifyNoMoreInteractions() is not recommended to use in every test method.
        verifyNoMoreInteractions() is a handy assertion from the interaction testing toolkit. Use it only when it's relevant.
        Abusing it leads to overspecified, less maintainable tests. You can find further reading
        <a href="http://monkeyisland.pl/2008/07/12/should-i-worry-about-the-unexpected/">here.
        See also Mockito#never() - it is more explicit and
        communicates the intent well.
        <h3 id="9">9. <a class="meaningful_link" href="#mock_annotation">Shorthand for mocks creation - @Mock annotation
        Minimizes repetitive mock creation code.
        Makes the test class more readable.
        Makes the verification error easier to read because the field name
        is used to identify the mock.
        <pre class="code"><code class="java">
        public class ArticleManagerTest {
        @Mock private ArticleCalculator calculator;
        @Mock private ArticleDatabase database;
        @Mock private UserProvider userProvider;
        private ArticleManager manager;
        Important! This needs to be somewhere in the base class or a test
        runner:
        <pre class="code"><code class="java">
        MockitoAnnotations.initMocks(testClass);
        You can use built-in runner: MockitoJUnitRunner or a rule: MockitoRule.
        Read more here: MockitoAnnotations
        <h3 id="10">10. <a class="meaningful_link" href="#stubbing_consecutive_calls">Stubbing consecutive calls (iterator-style stubbing)
        Sometimes we need to stub with different return value/exception for the same
        method call. Typical use case could be mocking iterators.
        Original version of Mockito did not have this feature to promote simple mocking.
        For example, instead of iterators one could use Iterable or simply
        collections. Those offer natural ways of stubbing (e.g. using real
        collections). In rare scenarios stubbing consecutive calls could be useful,
        though:
        <pre class="code"><code class="java">
        when(mock.someMethod("some arg"))
        .thenThrow(new RuntimeException())
        .thenReturn("foo");
        //First call: throws runtime exception:
        mock.someMethod("some arg");
        //Second call: prints "foo"
        System.out.println(mock.someMethod("some arg"));
        //Any consecutive call: prints "foo" as well (last stubbing wins).
        System.out.println(mock.someMethod("some arg"));
        Alternative, shorter version of consecutive stubbing:
        <pre class="code"><code class="java">
        when(mock.someMethod("some arg"))
        .thenReturn("one", "two", "three");
        <h3 id="11">11. <a class="meaningful_link" href="#answer_stubs">Stubbing with callbacks
        Allows stubbing with generic Answer interface.
        Yet another controversial feature which was not included in Mockito
        originally. We recommend simply stubbing with thenReturn() or
        thenThrow(), which should be enough to test/test-drive
        any clean & simple code. However, if you do have a need to stub with the generic Answer interface, here is an example:
        <pre class="code"><code class="java">
        when(mock.someMethod(anyString())).thenAnswer(new Answer() {
        Object answer(InvocationOnMock invocation) {
        Object[] args = invocation.getArguments();
        Object mock = invocation.getMock();
        return "called with arguments: " + args;
        }
        });
        //the following prints "called with arguments: foo"
        System.out.println(mock.someMethod("foo"));
        <h3 id="12">12. <a class="meaningful_link" href="#do_family_methods_stubs">doReturn()|doThrow()|
        doAnswer()|doNothing()|doCallRealMethod() family of methods
        Stubbing void methods requires a different approach from Mockito#when(Object) because the compiler does not
        like void methods inside brackets...
        Mockito#doThrow(Throwable...) replaces the Mockito#stubVoid(Object) method for stubbing voids.
        The main reason is improved readability and consistency with the family of doAnswer() methods.
        Use doThrow() when you want to stub a void method with an exception:
        <pre class="code"><code class="java">
        doThrow(new RuntimeException()).when(mockedList).clear();
        //following throws RuntimeException:
        mockedList.clear();
        You can use doThrow(), doAnswer(), doNothing(), doReturn()
        and doCallRealMethod() in place of the corresponding call with when(), for any method.
        It is necessary when you
        stub void methods
        stub methods on spy objects (see below)
        stub the same method more than once, to change the behaviour of a mock in the middle of a test.
        but you may prefer to use these methods in place of the alternative with when(), for all of your stubbing calls.
        Read more about these methods:
        Mockito#doReturn(Object)
        Mockito#doThrow(Throwable...)
        Mockito#doThrow(Class)
        Mockito#doAnswer(Answer)
        Mockito#doNothing()
        Mockito#doCallRealMethod()
        <h3 id="13">13. <a class="meaningful_link" href="#spy">Spying on real objects
        You can create spies of real objects. When you use the spy then the real methods are called
        (unless a method was stubbed).
        Real spies should be used carefully and occasionally, for example when dealing with legacy code.
        Spying on real objects can be associated with "partial mocking" concept.
        Before the release 1.8, Mockito spies were not real partial mocks.
        The reason was we thought partial mock is a code smell.
        At some point we found legitimate use cases for partial mocks
        (3rd party interfaces, interim refactoring of legacy code, the full article is <a href=
        "http://monkeyisland.pl/2009/01/13/subclass-and-override-vs-partial-mocking-vs-refactoring"
        >here)
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //optionally, you can stub out some methods:
        when(spy.size()).thenReturn(100);
        //using the spy calls *real* methods
        spy.add("one");
        spy.add("two");
        //prints "one" - the first element of a list
        System.out.println(spy.get(0));
        //size() method was stubbed - 100 is printed
        System.out.println(spy.size());
        //optionally, you can verify
        verify(spy).add("one");
        verify(spy).add("two");
        Important gotcha on spying real objects!
        Sometimes it's impossible or impractical to use Mockito#when(Object) for stubbing spies.
        Therefore when using spies please consider doReturn|Answer|Throw() family of
        methods for stubbing. Example:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing
        doReturn("foo").when(spy).get(0);
        Mockito *does not* delegate calls to the passed real instance, instead it actually creates a copy of it.
        So if you keep the real instance and interact with it, don't expect the spied to be aware of those interaction
        and their effect on real instance state.
        The corollary is that when an *unstubbed* method is called *on the spy* but *not on the real instance*,
        you won't see any effects on the real instance.
        Watch out for final methods.
        Mockito doesn't mock final methods so the bottom line is: when you spy on real objects + you try to stub a final method = trouble.
        Also you won't be able to verify those method as well.
        <h3 id="14">14. Changing <a class="meaningful_link" href="#defaultreturn">default return values of unstubbed invocations (Since 1.7)
        You can create a mock with specified strategy for its return values.
        It's quite an advanced feature and typically you don't need it to write decent tests.
        However, it can be helpful for working with legacy systems.
        It is the default answer so it will be used only when you don't stub the method call.
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, Mockito.RETURNS_SMART_NULLS);
        Foo mockTwo = mock(Foo.class, new YourOwnAnswer());
        Read more about this interesting implementation of Answer: Mockito#RETURNS_SMART_NULLS
        <h3 id="15">15. <a class="meaningful_link" href="#captors">Capturing arguments for further assertions (Since 1.8.0)
        Mockito verifies argument values in natural java style: by using an equals() method.
        This is also the recommended way of matching arguments because it makes tests clean & simple.
        In some situations though, it is helpful to assert on certain arguments after the actual verification.
        For example:
        <pre class="code"><code class="java">
        ArgumentCaptor&lt;Person&gt; argument = ArgumentCaptor.forClass(Person.class);
        verify(mock).doSomething(argument.capture());
        assertEquals("John", argument.getValue().getName());
        Warning: it is recommended to use ArgumentCaptor with verification but not with stubbing.
        Using ArgumentCaptor with stubbing may decrease test readability because captor is created outside of assert (aka verify or 'then') block.
        Also it may reduce defect localization because if stubbed method was not called then no argument is captured.
        In a way ArgumentCaptor is related to custom argument matchers (see javadoc for ArgumentMatcher class).
        Both techniques can be used for making sure certain arguments where passed to mocks.
        However, ArgumentCaptor may be a better fit if:
        custom argument matcher is not likely to be reused
        you just need it to assert on argument values to complete verification
        Custom argument matchers via ArgumentMatcher are usually better for stubbing.
        <h3 id="16">16. <a class="meaningful_link" href="#partial_mocks">Real partial mocks (Since 1.8.0)
        Finally, after many internal debates & discussions on the mailing list, partial mock support was added to Mockito.
        Previously we considered partial mocks as code smells. However, we found a legitimate use case for partial mocks - more reading:
        <a href="http://monkeyisland.pl/2009/01/13/subclass-and-override-vs-partial-mocking-vs-refactoring">here
        Before release 1.8 spy() was not producing real partial mocks and it was confusing for some users.
        Read more about spying: <a href="#13">here or in javadoc for Mockito#spy(Object) method.
        <pre class="code"><code class="java">
        //you can create partial mock with spy() method:
        List list = spy(new LinkedList());
        //you can enable partial mock capabilities selectively on mocks:
        Foo mock = mock(Foo.class);
        //Be sure the real implementation is 'safe'.
        //If real implementation throws exceptions or depends on specific state of the object then you're in trouble.
        when(mock.someMethod()).thenCallRealMethod();
        As usual you are going to read the partial mock warning:
        Object oriented programming is more less tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        <h3 id="17">17. <a class="meaningful_link" href="#resetting_mocks">Resetting mocks (Since 1.8.0)
        Smart Mockito users hardly use this feature because they know it could be a sign of poor tests.
        Normally, you don't need to reset your mocks, just create new mocks for each test method.
        Instead of reset() please consider writing simple, small and focused test methods over lengthy, over-specified tests.
        First potential code smell is reset() in the middle of the test method. This probably means you're testing too much.
        Follow the whisper of your test methods: "Please keep us small & focused on single behavior".
        There are several threads about it on mockito mailing list.
        The only reason we added reset() method is to
        make it possible to work with container-injected mocks.
        See issue 55 (<a href="http://code.google.com/p/mockito/issues/detail?id=55">here)
        or FAQ (<a href="http://code.google.com/p/mockito/wiki/FAQ">here).
        Don't harm yourself. reset() in the middle of the test method is a code smell (you're probably testing too much).
        <pre class="code"><code class="java">
        List mock = mock(List.class);
        when(mock.size()).thenReturn(10);
        mock.add(1);
        reset(mock);
        //at this point the mock forgot any interactions & stubbing
        <h3 id="18">18. <a class="meaningful_link" href="#framework_validation">Troubleshooting & validating framework usage (Since 1.8.0)
        First of all, in case of any trouble, I encourage you to read the Mockito FAQ:
        <a href="http://code.google.com/p/mockito/wiki/FAQ">http://code.google.com/p/mockito/wiki/FAQ
        In case of questions you may also post to mockito mailing list:
        <a href="http://groups.google.com/group/mockito">http://groups.google.com/group/mockito
        Next, you should know that Mockito validates if you use it correctly all the time.
        However, there's a gotcha so please read the javadoc for Mockito#validateMockitoUsage()
        <h3 id="19">19. <a class="meaningful_link" href="#bdd_mockito">Aliases for behavior driven development (Since 1.8.0)
        Behavior Driven Development style of writing tests uses //given //when //then comments as fundamental parts of your test methods.
        This is exactly how we write our tests and we warmly encourage you to do so!
        Start learning about BDD here: <a href="http://en.wikipedia.org/wiki/Behavior_Driven_Development">http://en.wikipedia.org/wiki/Behavior_Driven_Development
        The problem is that current stubbing api with canonical role of when word does not integrate nicely with //given //when //then comments.
        It's because stubbing belongs to given component of the test and not to the when component of the test.
        Hence BDDMockito class introduces an alias so that you stub method calls with BDDMockito#given(Object) method.
        Now it really nicely integrates with the given component of a BDD style test!
        Here is how the test might look like:
        <pre class="code"><code class="java">
        import static org.mockito.BDDMockito.*;
        Seller seller = mock(Seller.class);
        Shop shop = new Shop(seller);
        public void shouldBuyBread() throws Exception {
        //given
        given(seller.askForBread()).willReturn(new Bread());
        //when
        Goods goods = shop.buyBread();
        //then
        assertThat(goods, containBread());
        }
        <h3 id="20">20. <a class="meaningful_link" href="#serializable_mocks">Serializable mocks (Since 1.8.1)
        Mocks can be made serializable. With this feature you can use a mock in a place that requires dependencies to be serializable.
        WARNING: This should be rarely used in unit testing.
        The behaviour was implemented for a specific use case of a BDD spec that had an unreliable external dependency.  This
        was in a web environment and the objects from the external dependency were being serialized to pass between layers.
        To create serializable mock use MockSettings#serializable():
        <pre class="code"><code class="java">
        List serializableMock = mock(List.class, withSettings().serializable());
        The mock can be serialized assuming all the normal <a href='http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html'>
        serialization requirements are met by the class.
        Making a real object spy serializable is a bit more effort as the spy(...) method does not have an overloaded version
        which accepts MockSettings. No worries, you will hardly ever use it.
        <pre class="code"><code class="java">
        List&lt;Object&gt; list = new ArrayList&lt;Object&gt;();
        List&lt;Object&gt; spy = mock(ArrayList.class, withSettings()
        .spiedInstance(list)
        .defaultAnswer(CALLS_REAL_METHODS)
        .serializable());
        <h3 id="21">21. New annotations: <a class="meaningful_link" href="#captor_annotation">@Captor,
        <a class="meaningful_link" href="#spy_annotation">@Spy,
        <a class="meaningful_link" href="#injectmocks_annotation">@InjectMocks (Since 1.8.3)
        Release 1.8.3 brings new annotations that may be helpful on occasion:
        @Captor simplifies creation of ArgumentCaptor
        - useful when the argument to capture is a nasty generic class and you want to avoid compiler warnings
        @Spy - you can use it instead Mockito#spy(Object).
        @InjectMocks - injects mock or spy fields into tested object automatically.
        Note that @InjectMocks can also be used in combination with the @Spy annotation, it means
        that Mockito will inject mocks into the partial mock under test. This complexity is another good reason why you
        should only use partial mocks as a last resort. See point 16 about partial mocks.
        All new annotations are *only* processed on MockitoAnnotations#initMocks(Object).
        Just like for @Mock annotation you can use the built-in runner: MockitoJUnitRunner or rule:
        MockitoRule.
        <h3 id="22">22. <a class="meaningful_link" href="#verification_timeout">Verification with timeout (Since 1.8.5)
        Allows verifying with timeout. It causes a verify to wait for a specified period of time for a desired
        interaction rather than fails immediately if had not already happened. May be useful for testing in concurrent
        conditions.
        It feels this feature should be used rarely - figure out a better way of testing your multi-threaded system.
        Not yet implemented to work with InOrder verification.
        Examples:
        <pre class="code"><code class="java">
        //passes when someMethod() is called within given time span
        verify(mock, timeout(100)).someMethod();
        //above is an alias to:
        verify(mock, timeout(100).times(1)).someMethod();
        //passes when someMethod() is called *exactly* 2 times within given time span
        verify(mock, timeout(100).times(2)).someMethod();
        //passes when someMethod() is called *at least* 2 times within given time span
        verify(mock, timeout(100).atLeast(2)).someMethod();
        //verifies someMethod() within given time span using given verification mode
        //useful only if you have your own custom verification modes.
        verify(mock, new Timeout(100, yourOwnVerificationMode)).someMethod();
        <h3 id="23">23. <a class="meaningful_link" href="#automatic_instantiation">Automatic instantiation of @Spies,
        @InjectMocks and <a class="meaningful_link" href="#constructor_injection">constructor injection goodness (Since 1.9.0)
        Mockito will now try to instantiate @Spy and will instantiate @InjectMocks fields
        using constructor injection, setter injection, or field injection.
        To take advantage of this feature you need to use MockitoAnnotations#initMocks(Object), MockitoJUnitRunner
        or MockitoRule.
        Read more about available tricks and the rules of injection in the javadoc for InjectMocks
        <pre class="code"><code class="java">
        //instead:
        @Spy BeerDrinker drinker = new BeerDrinker();
        //you can write:
        @Spy BeerDrinker drinker;
        //same applies to @InjectMocks annotation:
        @InjectMocks LocalPub;
        <h3 id="24">24. <a class="meaningful_link" href="#one_liner_stub">One-liner stubs (Since 1.9.0)
        Mockito will now allow you to create mocks when stubbing.
        Basically, it allows to create a stub in one line of code.
        This can be helpful to keep test code clean.
        For example, some boring stub can be created & stubbed at field initialization in a test:
        <pre class="code"><code class="java">
        public class CarTest {
        Car boringStubbedCar = when(mock(Car.class).shiftGear()).thenThrow(EngineNotStarted.class).getMock();
        @Test public void should... {}
        <h3 id="25">25. <a class="meaningful_link" href="#ignore_stubs_verification">Verification ignoring stubs (Since 1.9.0)
        Mockito will now allow to ignore stubbing for the sake of verification.
        Sometimes useful when coupled with verifyNoMoreInteractions() or verification inOrder().
        Helps avoiding redundant verification of stubbed calls - typically we're not interested in verifying stubs.
        Warning, ignoreStubs() might lead to overuse of verifyNoMoreInteractions(ignoreStubs(...));
        Bear in mind that Mockito does not recommend bombarding every test with verifyNoMoreInteractions()
        for the reasons outlined in javadoc for Mockito#verifyNoMoreInteractions(Object...)
        Some examples:
        <pre class="code"><code class="java">
        verify(mock).foo();
        verify(mockTwo).bar();
        //ignores all stubbed methods:
        verifyNoMoreInvocations(ignoreStubs(mock, mockTwo));
        //creates InOrder that will ignore stubbed
        InOrder inOrder = inOrder(ignoreStubs(mock, mockTwo));
        inOrder.verify(mock).foo();
        inOrder.verify(mockTwo).bar();
        inOrder.verifyNoMoreInteractions();
        Advanced examples and more details can be found in javadoc for Mockito#ignoreStubs(Object...)
        <h3 id="26">26. <a class="meaningful_link" href="#mocking_details">Mocking details (Since 1.9.5)
        To identify whether a particular object is a mock or a spy:
        <pre class="code"><code class="java">
        Mockito.mockingDetails(someObject).isMock();
        Mockito.mockingDetails(someObject).isSpy();
        Both the MockingDetails#isMock and MockingDetails#isSpy() methods return boolean.
        As a spy is just a different kind of mock, isMock() returns true if the object is a spy.
        In future Mockito versions MockingDetails may grow and provide other useful information about the mock,
        e.g. invocations, stubbing info, etc.
        <h3 id="27">27. <a class="meaningful_link" href="#delegating_call_to_real_instance">Delegate calls to real instance (Since 1.9.5)
        Useful for spies or partial mocks of objects that are difficult to mock or spy using the usual spy API.
        Since Mockito 1.10.11, the delegate may or may not be of the same type as the mock.
        If the type is different, a matching method needs to be found on delegate type otherwise an exception is thrown.
        Possible use cases for this feature:
        Final classes but with an interface
        Already custom proxied object
        Special objects with a finalize method, i.e. to avoid executing it 2 times
        The difference with the regular spy:
        The regular spy (#spy(Object)) contains all state from the spied instance
        and the methods are invoked on the spy. The spied instance is only used at mock creation to copy the state from.
        If you call a method on a regular spy and it internally calls other methods on this spy, those calls are remembered
        for verifications, and they can be effectively stubbed.
        The mock that delegates simply delegates all methods to the delegate.
        The delegate is used all the time as methods are delegated onto it.
        If you call a method on a mock that delegates and it internally calls other methods on this mock,
        those calls are not remembered for verifications, stubbing does not have effect on them, too.
        Mock that delegates is less powerful than the regular spy but it is useful when the regular spy cannot be created.
        See more information in docs for AdditionalAnswers#delegatesTo(Object).
        <h3 id="28">28. <a class="meaningful_link" href="#mock_maker_plugin">MockMaker API (Since 1.9.5)
        Driven by requirements and patches from Google Android guys Mockito now offers an extension point
        that allows replacing the proxy generation engine. By default, Mockito uses cglib to create dynamic proxies.
        The extension point is for advanced users that want to extend Mockito. For example, it is now possible
        to use Mockito for Android testing with a help of dexmaker.
        For more details, motivations and examples please refer to
        the docs for org.mockito.plugins.MockMaker.
        <h3 id="29">29. <a class="meaningful_link" href="#BDD_behavior_verification">(new) BDD style verification (Since 1.10.0)
        Enables Behavior Driven Development (BDD) style verification by starting verification with the BDD then keyword.
        <pre class="code"><code class="java">
        given(dog.bark()).willReturn(2);
        // when
        ...
        then(person).should(times(2)).ride(bike);
        For more information and an example see BDDMockito#then(Object)}
        <h3 id="30">30. <a class="meaningful_link" href="#spying_abstract_classes">(new) Spying or mocking abstract classes (Since 1.10.12)
        It is now possible to conveniently spy on abstract classes. Note that overusing spies hints at code design smells (see #spy(Object)).
        Previously, spying was only possible on instances of objects.
        New API makes it possible to use constructor when creating an instance of the mock.
        This is particularly useful for mocking abstract classes because the user is no longer required to provide an instance of the abstract class.
        At the moment, only parameter-less constructor is supported, let us know if it is not enough.
        <pre class="code"><code class="java">
        //convenience API, new overloaded spy() method:
        SomeAbstract spy = spy(SomeAbstract.class);
        //Robust API, via settings builder:
        OtherAbstract spy = mock(OtherAbstract.class, withSettings()
        .useConstructor().defaultAnswer(CALLS_REAL_METHODS));
        //Mocking a non-static inner abstract class:
        InnerAbstract spy = mock(InnerAbstract.class, withSettings()
        .useConstructor().outerInstance(outerInstance).defaultAnswer(CALLS_REAL_METHODS));
        For more information please see MockSettings#useConstructor().
        <h3 id="31">31. <a class="meaningful_link" href="#serilization_across_classloader">(new) Mockito mocks can be serialized / deserialized across classloaders (Since 1.10.0)
        Mockito introduces serialization across classloader.
        Like with any other form of serialization, all types in the mock hierarchy have to serializable, inclusing answers.
        As this serialization mode require considerably more work, this is an opt-in setting.
        <pre class="code"><code class="java">
        // use regular serialization
        mock(Book.class, withSettings().serializable());
        // use serialization across classloaders
        mock(Book.class, withSettings().serializable(ACROSS_CLASSLOADERS));
        For more details see MockSettings#serializable(SerializableMode).
        <h3 id="32">32. <a class="meaningful_link" href="#better_generic_support_with_deep_stubs">(new) Better generic support with deep stubs (Since 1.10.0)
        Deep stubbing has been improved to find generic information if available in the class.
        That means that classes like this can be used without having to mock the behavior.
        <pre class="code"><code class="java">
        class Lines extends List&lt;Line&gt; {
        // ...
        }
        lines = mock(Lines.class, RETURNS_DEEP_STUBS);
        // Now Mockito understand this is not an Object but a Line
        Line line = lines.iterator().next();
        Please note that in most scenarios a mock returning a mock is wrong.
        <h3 id="33">33. <a class="meaningful_link" href="#mockito_junit_rule">(new) Mockito JUnit rule (Since 1.10.17)
        Mockito now offers a JUnit rule. Until now in JUnit there was two wasy to initialize fields annotated by Mockito annotations
        such as @Mock, @Spy, @InjectMocks, etc.
        Annotating the JUnit test class with a @org.junit.runner.RunWith(MockitoJUnitRunner.class)
        Invoking MockitoAnnotations#initMocks(Object) in the @org.junit.Before method
        Now you can choose to use a rule :
        <pre class="code"><code class="java">
        @RunWith(YetAnotherRunner.class)
        public class TheTest {
        @Rule public MockitoRule mockito = MockitoJUnit.rule();
        // ...
        }
        For more information see MockitoJUnit#rule().
        <h3 id="34">34. <a class="meaningful_link" href="#plugin_switch">(new) Switch on or off plugins (Since 1.10.15)
        An incubating feature made it's way in mockito that will allow to toggle a mockito-plugin.
        More information here org.mockito.plugins.PluginSwitch.
        <h3 id="35">35. <a class="meaningful_link" href="#BDD_behavior_verification">Custom verification failure message (Since 2.0.0)
        Allows specifying a custom message to be printed if verification fails.
        Examples:
        <pre class="code"><code class="java">
        // will print a custom message on verification failure
        verify(mock, description("This will print on failure")).someMethod();
        // will work with any verification mode
        verify(mock, times(2).description("someMethod should be called twice")).someMethod();
        TODO rework the documentation, write about hamcrest.

# File: `AdditionalMatchers.java`

## Method: `public static boolean or(boolean first, boolean second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean or(boolean first, boolean second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->boolean argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return false.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static T or(T first, T second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T or(T first, T second)", "entityFile": "AdditionalMatchers.java"} -->Object argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param <T>
        the type of the object, it is passed through to prevent casts.
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return null.

## Method: `public static short or(short first, short second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short or(short first, short second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->short argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.
        <!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static long or(long first, long second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long or(long first, long second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->long argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

# File: `MockitoAnnotations.java`

## Annotation: `Mock`

        <!-- META {"entityType": "Annotation", "entitySignature": "Mock", "entityFile": "MockitoAnnotations.java"} -->Use top-level org.mockito.Mock annotation instead
        When @Mock annotation was implemented as an inner class then users experienced problems with autocomplete features in IDEs.
        Hence @Mock was made a top-level class.
        How to fix deprecation warnings?
        Typically, you can just search: import org.mockito.MockitoAnnotations.Mock; and replace with: import org.mockito.Mock;
        If you're an existing user then sorry for making your code littered with deprecation warnings.
        This change was required to make Mockito better.

## Method: `public static void initMocks(Object testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void initMocks(Object testClass)", "entityFile": "MockitoAnnotations.java"} -->Initializes objects annotated with Mockito annotations for given testClass:
        @org.mockito.Mock, @Spy, @Captor, @InjectMocks
        See examples in javadoc for MockitoAnnotations class.

# File: `AdditionalMatchers.java`

## Method: `public static int or(int first, int second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int or(int first, int second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->int argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static float or(float first, float second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float or(float first, float second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->float argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static double or(double first, double second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double or(double first, double second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->double argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

# File: `MockitoAnnotations.java`

## Class: `MockitoAnnotations`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoAnnotations", "entityFile": "MockitoAnnotations.java"} -->MockitoAnnotations.initMocks(this); initializes fields annotated with Mockito annotations.
        Allows shorthand creation of objects required for testing.
        Minimizes repetitive mock creation code.
        Makes the test class more readable.
        Makes the verification error easier to read because field name is used to identify the mock.
        <pre class="code"><code class="java">
        public class ArticleManagerTest extends SampleBaseTestCase {
        @Mock private ArticleCalculator calculator;
        @Mock private ArticleDatabase database;
        @Mock private UserProvider userProvider;
        private ArticleManager manager;
        @Before public void setup() {
        manager = new ArticleManager(userProvider, database, calculator);
        }
        }
        public class SampleBaseTestCase {
        @Before public void initMocks() {
        MockitoAnnotations.initMocks(this);
        }
        }
        Read also about other annotations @Spy, @Captor, @InjectMocks
        MockitoAnnotations.initMocks(this) method has to called to initialize annotated fields.
        In above example, initMocks() is called in @Before (JUnit4) method of test's base class.
        For JUnit3 initMocks() can go to setup() method of a base class.
        You can also put initMocks() in your JUnit runner (@RunWith) or use built-in runner: MockitoJUnitRunner

# File: `AdditionalMatchers.java`

## Method: `public static char or(char first, char second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char or(char first, char second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->char argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static byte or(byte first, byte second)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte or(byte first, byte second)", "entityFile": "AdditionalMatchers.java"} --><!-- ba70c3f8-1789-11ea-836f-333445793454 <=< ACCEPT -->byte argument that matches any of the given argument matchers.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the first argument matcher.
        @param second
        placeholder for the second argument matcher.
        @return 0.<!-- ACCEPT >=> ba70c3f8-1789-11ea-836f-333445793454 -->

## Method: `public static T not(T first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T not(T first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->Object argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param <T>
        the type of the object, it is passed through to prevent casts.
        @param first
        placeholder for the argument matcher.
        @return null.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static short not(short first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static short not(short first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->short argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static int not(int first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static int not(int first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->int argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.
        <!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

# File: `MockSettings.java`

## Method: `MockSettings extraInterfaces(Class<?>... interfaces)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings extraInterfaces(Class<?>... interfaces)", "entityFile": "MockSettings.java"} -->Specifies extra interfaces the mock should implement. Might be useful for legacy code or some corner cases.
        For background, see issue 51 <a href="http://code.google.com/p/mockito/issues/detail?id=51">here
        This mysterious feature should be used very occasionally.
        The object under test should know exactly its collaborators & dependencies.
        If you happen to use it often than please make sure you are really producing simple, clean & readable code.
        Examples:
        <pre class="code"><code class="java">
        Foo foo = mock(Foo.class, withSettings().extraInterfaces(Bar.class, Baz.class));
        //now, the mock implements extra interfaces, so following casting is possible:
        Bar bar = (Bar) foo;
        Baz baz = (Baz) foo;
        @param interfaces extra interfaces the should implement.
        @return settings instance so that you can fluently specify other settings

# File: `AdditionalMatchers.java`

## Method: `public static long not(long first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static long not(long first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->long argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static float not(float first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float not(float first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->float argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.
        <!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static double not(double first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double not(double first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->double argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static char not(char first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static char not(char first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->char argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

# File: `MockSettings.java`

## Method: `MockSettings name(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings name(String name)", "entityFile": "MockSettings.java"} -->Specifies mock name. Naming mocks can be helpful for debugging - the name is used in all verification errors.
        Beware that naming mocks is not a solution for complex code which uses too many mocks or collaborators.
        If you have too many mocks then refactor the code so that it's easy to test/debug without necessity of naming mocks.
        If you use @Mock annotation then you've got naming mocks for free! @Mock uses field name as mock name. Mock Read more.
        Examples:
        <pre class="code"><code class="java">
        Foo foo = mock(Foo.class, withSettings().name("foo"));
        //Below does exactly the same:
        Foo foo = mock(Foo.class, "foo");
        @param name the name of the mock, later used in all verification errors
        @return settings instance so that you can fluently specify other settings

# File: `AdditionalMatchers.java`

## Method: `public static boolean not(boolean first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean not(boolean first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->boolean argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return false.<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->

## Method: `public static byte not(byte first)`

        <!-- META {"entityType": "Method", "entitySignature": "public static byte not(byte first)", "entityFile": "AdditionalMatchers.java"} --><!-- 66bbf828-178a-11ea-9224-333445793454 <=< ACCEPT -->byte argument that does not match the given argument matcher.
        See examples in javadoc for AdditionalMatchers class
        @param first
        placeholder for the argument matcher.
        @return 0<!-- ACCEPT >=> 66bbf828-178a-11ea-9224-333445793454 -->.

# File: `MockSettings.java`

## Method: `MockSettings spiedInstance(Object instance)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings spiedInstance(Object instance)", "entityFile": "MockSettings.java"} -->Specifies the instance to spy on. Makes sense only for spies/partial mocks.
        Sets the instance that will be spied. Actually copies the internal fields of the passed instance to the mock.
        As usual you are going to read the partial mock warning:
        Object oriented programming is more or less about tackling complexity by dividing the complexity into separate, specific, SRPy objects.
        How does partial mock fit into this paradigm? Well, it just doesn't...
        Partial mock usually means that the complexity has been moved to a different method on the same object.
        In most cases, this is not the way you want to design your application.
        However, there are rare cases when partial mocks come handy:
        dealing with code you cannot change easily (3rd party interfaces, interim refactoring of legacy code etc.)
        However, I wouldn't use partial mocks for new, test-driven & well-designed code.
        Enough warnings about partial mocks, see an example how spiedInstance() works:
        <pre class="code"><code class="java">
        Foo foo = mock(Foo.class, withSettings().spiedInstance(fooInstance));
        //Below does exactly the same:
        Foo foo = spy(fooInstance);
        About stubbing for a partial mock, as it is a spy it will always call the real method, unless you use the
        doReturn|Throw|Answer|CallRealMethod stubbing style. Example:
        <pre class="code"><code class="java">
        List list = new LinkedList();
        List spy = spy(list);
        //Impossible: real method is called so spy.get(0) throws IndexOutOfBoundsException (the list is yet empty)
        when(spy.get(0)).thenReturn("foo");
        //You have to use doReturn() for stubbing
        doReturn("foo").when(spy).get(0);
        @param instance to spy on
        @return settings instance so that you can fluently specify other settings

# File: `AdditionalMatchers.java`

## Method: `public static double eq(double value, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static double eq(double value, double delta)", "entityFile": "AdditionalMatchers.java"} -->double argument that has an absolute difference to the given value that
        is less than the given delta details.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @param delta
        the given delta.
        @return 0.

## Method: `public static float eq(float value, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static float eq(float value, float delta)", "entityFile": "AdditionalMatchers.java"} -->float argument that has an absolute difference to the given value that is
        less than the given delta details.
        See examples in javadoc for AdditionalMatchers class
        @param value
        the given value.
        @param delta
        the given delta.
        @return 0.

# File: `MockSettings.java`

## Method: `MockSettings defaultAnswer(Answer defaultAnswer)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings defaultAnswer(Answer defaultAnswer)", "entityFile": "MockSettings.java"} --><!-- 90596ef4-1782-11ea-8ba9-333445793454 <=< ACCEPT -->Specifies default answers to interactions.
        It's quite advanced feature and typically you don't need it to write decent tests.
        However it can be helpful when working with legacy systems.
        It is the default answer so it will be used only when you don't stub the method call.
        <pre class="code"><code class="java">
        Foo mock = mock(Foo.class, withSettings().defaultAnswer(RETURNS_SMART_NULLS));
        Foo mockTwo = mock(Foo.class, withSettings().defaultAnswer(new YourOwnAnswer()));
        //Below does exactly the same:
        Foo mockTwo = mock(Foo.class, new YourOwnAnswer());
        @param defaultAnswer default answer to be used by mock when not stubbed
        @return settings instance so that you can fluently specify other settings<!-- ACCEPT >=> 90596ef4-1782-11ea-8ba9-333445793454 -->

# File: `AdditionalMatchers.java`

## Class: `AdditionalMatchers`

        <!-- META {"entityType": "Class", "entitySignature": "AdditionalMatchers", "entityFile": "AdditionalMatchers.java"} -->See Matchers for general info about matchers.
        AdditionalMatchers provides rarely used matchers, kept only for somewhat compatibility with EasyMock.
        Use additional matchers very judiciously because they may impact readability of a test.
        It is recommended to use matchers from Matchers and keep stubbing and verification simple.
        Example of using logical and(), not(), or() matchers:
        <pre class="code"><code class="java">
        //anything but not "ejb"
        mock.someMethod(not(eq("ejb")));
        //not "ejb" and not "michael jackson"
        mock.someMethod(and(not(eq("ejb")), not(eq("michael jackson"))));
        //1 or 10
        mock.someMethod(or(eq(1), eq(10)));
        Scroll down to see all methods - full list of matchers.

# File: `MockSettings.java`

## Method: `MockSettings serializable()`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings serializable()", "entityFile": "MockSettings.java"} -->Configures the mock to be serializable. With this feature you can use a mock in a place that requires dependencies to be serializable.
        WARNING: This should be rarely used in unit testing.
        The behaviour was implemented for a specific use case of a BDD spec that had an unreliable external dependency.  This
        was in a web environment and the objects from the external dependency were being serialized to pass between layers.
        Example:
        <pre class="code"><code class="java">
        List serializableMock = mock(List.class, withSettings().serializable());
        @return settings instance so that you can fluently specify other settings
        @since 1.8.1

## Method: `MockSettings serializable(SerializableMode mode)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings serializable(SerializableMode mode)", "entityFile": "MockSettings.java"} -->Configures the mock to be serializable with a specific serializable mode.
        With this feature you can use a mock in a place that requires dependencies to be serializable.
        WARNING: This should be rarely used in unit testing.
        The behaviour was implemented for a specific use case of a BDD spec that had an unreliable external dependency.  This
        was in a web environment and the objects from the external dependency were being serialized to pass between layers.
        <pre class="code"><code class="java">
        List serializableMock = mock(List.class, withSettings().serializable(SerializableMode.ACROSS_CLASSLOADERS));
        @param mode serialization mode
        @return settings instance so that you can fluently specify other settings
        @since 1.10.0

# File: `Answers.java`

## EnumConstant: `RETURNS_DEFAULTS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "RETURNS_DEFAULTS", "entityFile": "Answers.java"} -->The default configured answer of every mock.
        Please see the org.mockito.Mockito#RETURNS_DEFAULTS documentation for more details.
        @see org.mockito.Mockito#RETURNS_DEFAULTS

## EnumConstant: `RETURNS_SMART_NULLS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "RETURNS_SMART_NULLS", "entityFile": "Answers.java"} -->An answer that returns smart-nulls.
        Please see the org.mockito.Mockito#RETURNS_SMART_NULLS documentation for more details.
        @see org.mockito.Mockito#RETURNS_SMART_NULLS

## EnumConstant: `RETURNS_MOCKS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "RETURNS_MOCKS", "entityFile": "Answers.java"} -->An answer that returns mocks (not stubs).
        Please see the org.mockito.Mockito#RETURNS_MOCKS documentation for more details.
        @see org.mockito.Mockito#RETURNS_MOCKS

# File: `MockSettings.java`

## Method: `MockSettings verboseLogging()`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings verboseLogging()", "entityFile": "MockSettings.java"} -->Enables real-time logging of method invocations on this mock. Can be used
        during test debugging in order to find wrong interactions with this mock.
        Invocations are logged as they happen to the standard output stream.
        Calling this method multiple times makes no difference.
        Example:
        <pre class="code"><code class="java">
        List mockWithLogger = mock(List.class, withSettings().verboseLogging());
        @return settings instance so that you can fluently specify other settings

# File: `Answers.java`

## EnumConstant: `RETURNS_DEEP_STUBS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "RETURNS_DEEP_STUBS", "entityFile": "Answers.java"} -->An answer that returns deep stubs (not mocks).
        Please see the org.mockito.Mockito#RETURNS_DEEP_STUBS documentation for more details.
        @see org.mockito.Mockito#RETURNS_DEEP_STUBS

## EnumConstant: `CALLS_REAL_METHODS`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "CALLS_REAL_METHODS", "entityFile": "Answers.java"} -->An answer that calls the real methods (used for partial mocks).
        Please see the org.mockito.Mockito#CALLS_REAL_METHODS documentation for more details.
        @see org.mockito.Mockito#CALLS_REAL_METHODS

## EnumConstant: `RETURNS_SELF`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "RETURNS_SELF", "entityFile": "Answers.java"} -->An answer that tries to return itself. This is useful for mocking Builders.
        Please see the org.mockito.Mockito#RETURNS_SELF documentation for more details.
        @see org.mockito.Mockito#RETURNS_SELF

# File: `MockSettings.java`

## Method: `MockSettings invocationListeners(InvocationListener... listeners)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings invocationListeners(InvocationListener... listeners)", "entityFile": "MockSettings.java"} -->Registers a listener for method invocations on this mock. The listener is
        notified every time a method on this mock is called.
        Multiple listeners may be added, but the same object is only added once.
        The order, in which the listeners are added, is not guaranteed to be the
        order in which the listeners are notified.
        Example:
        <pre class="code"><code class="java">
        List mockWithListener = mock(List.class, withSettings().invocationListeners(new YourInvocationListener()));
        See the InvocationListener listener interface for more details.
        @param listeners The invocation listeners to add. May not be null.
        @return settings instance so that you can fluently specify other settings

## Method: `MockSettings stubOnly()`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings stubOnly()", "entityFile": "MockSettings.java"} -->A stub-only mock does not record method
        invocations, thus saving memory but
        disallowing verification of invocations.
        Example:
        <pre class="code"><code class="java">
        List stubOnly = mock(List.class, withSettings().stubOnly());
        @return settings instance so that you can fluently specify other settings

# File: `Answers.java`

## Method: `public Answer<Object> get()`

        <!-- META {"entityType": "Method", "entitySignature": "public Answer<Object> get()", "entityFile": "Answers.java"} -->@deprecated Use the enum-constant directly, instead of this getter. This method will be removed in a future release
        E.g. instead of Answers.CALLS_REAL_METHODS.get() use Answers.CALLS_REAL_METHODS .

# File: `MockSettings.java`

## Method: `MockSettings useConstructor()`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings useConstructor()", "entityFile": "MockSettings.java"} -->Mockito attempts to use constructor when creating instance of the mock.
        This is particularly useful for spying on abstract classes. See also Mockito#spy(Class).
        Example:
        <pre class="code"><code class="java">
        //Robust API, via settings builder:
        OtherAbstract spy = mock(OtherAbstract.class, withSettings()
        .useConstructor().defaultAnswer(CALLS_REAL_METHODS));
        //Mocking a non-static inner abstract class:
        InnerAbstract spy = mock(InnerAbstract.class, withSettings()
        .useConstructor().outerInstance(outerInstance).defaultAnswer(CALLS_REAL_METHODS));
        @return settings instance so that you can fluently specify other settings
        @since 1.10.12

# File: `Answers.java`

## Enum: `Answers`

        <!-- META {"entityType": "Enum", "entitySignature": "Answers", "entityFile": "Answers.java"} -->Enumeration of pre-configured mock answers
        You can use it to pass extra parameters to @Mock annotation, see more info here: Mock
        Example:
        <pre class="code"><code class="java">
        @Mock(answer = RETURNS_DEEP_STUBS) UserProvider userProvider;
        This is not the full list of Answers available in Mockito. Some interesting answers can be found in org.mockito.stubbing.answers package.

# File: `MockSettings.java`

## Method: `MockSettings outerInstance(Object outerClassInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "MockSettings outerInstance(Object outerClassInstance)", "entityFile": "MockSettings.java"} -->Makes it possible to mock non-static inner classes in conjunction with #useConstructor().
        Example:
        <pre class="code"><code class="java">
        InnerClass mock = mock(InnerClass.class, withSettings()
        .useConstructor().outerInstance(outerInstance).defaultAnswer(CALLS_REAL_METHODS));
        @return settings instance so that you can fluently specify other settings
        @since 1.10.12

## Interface: `MockSettings`

        <!-- META {"entityType": "Interface", "entitySignature": "MockSettings", "entityFile": "MockSettings.java"} --><!-- 3b872434-1785-11ea-b96e-333445793454 <=< ACCEPT -->Allows mock creation with additional mock settings.
        Don't use it too often.
        Consider writing simple tests that use simple mocks.
        Repeat after me: simple tests push simple, KISSy, readable & maintainable code.
        If you cannot write a test in a simple way - refactor the code under test.
        Examples of mock settings:
        <pre class="code"><code class="java">
        //Creates mock with different default answer & name
        Foo mock = mock(Foo.class, withSettings()
        .defaultAnswer(RETURNS_SMART_NULLS)
        .name("cool mockie")
        );
        //Creates mock with different default answer, descriptive name and extra interfaces
        Foo mock = mock(Foo.class, withSettings()
        .defaultAnswer(RETURNS_SMART_NULLS)
        .name("cool mockie")
        .extraInterfaces(Bar.class));
        MockSettings has been introduced for two reasons.
        Firstly, to make it easy to add another mock setting when the demand comes.
        Secondly, to enable combining together different mock settings without introducing zillions of overloaded mock() methods.<!-- ACCEPT >=> 3b872434-1785-11ea-b96e-333445793454 -->

# File: `ArgumentCaptor.java`

## Method: `public ArgumentCaptor()`

        <!-- META {"entityType": "Method", "entitySignature": "public ArgumentCaptor()", "entityFile": "ArgumentCaptor.java"} -->@deprecated
        Please use factory method ArgumentCaptor#forClass(Class) to create captors
        This is required to avoid NullPointerExceptions when autoUnboxing primitive types.
        See issue 99.
        Example:
        <pre class="code"><code class="java">
        ArgumentCaptor&lt;Person&gt; argument = ArgumentCaptor.forClass(Person.class);
        verify(mock).doSomething(argument.capture());
        assertEquals("John", argument.getValue().getName());

## Method: `public T capture()`

        <!-- META {"entityType": "Method", "entitySignature": "public T capture()", "entityFile": "ArgumentCaptor.java"} -->Use it to capture the argument. This method must be used inside of verification.
        Internally, this method registers a special implementation of an ArgumentMatcher.
        This argument matcher stores the argument value so that you can use it later to perform assertions.
        See examples in javadoc for ArgumentCaptor class.
        @return null or default values

## Method: `public T getValue()`

        <!-- META {"entityType": "Method", "entitySignature": "public T getValue()", "entityFile": "ArgumentCaptor.java"} -->Returns the captured value of the argument. When capturing varargs use #getAllValues().
        If verified method was called multiple times then this method it returns the latest captured value.
        See examples in javadoc for ArgumentCaptor class.
        @return captured argument value

## Method: `public List<T> getAllValues()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<T> getAllValues()", "entityFile": "ArgumentCaptor.java"} -->Returns all captured values. Use it when capturing varargs or when the verified method was called multiple times.
        When varargs method was called multiple times, this method returns merged list of all values from all invocations.
        Example:
        <pre class="code"><code class="java">
        mock.doSomething(new Person("John");
        mock.doSomething(new Person("Jane");
        ArgumentCaptor&lt;Person&gt; peopleCaptor = ArgumentCaptor.forClass(Person.class);
        verify(mock, times(2)).doSomething(peopleCaptor.capture());
        List&lt;Person&gt; capturedPeople = peopleCaptor.getAllValues();
        assertEquals("John", capturedPeople.get(0).getName());
        assertEquals("Jane", capturedPeople.get(1).getName());
        Example of capturing varargs:
        <pre class="code"><code class="java">
        mock.countPeople(new Person("John"), new Person("Jane"); //vararg method
        ArgumentCaptor&lt;Person&gt; peopleCaptor = ArgumentCaptor.forClass(Person.class);
        verify(mock).countPeople(peopleCaptor.capture());
        List expected = asList(new Person("John"), new Person("Jane"));
        assertEquals(expected, peopleCaptor.getAllValues());
        See more examples in javadoc for ArgumentCaptor class.
        @return captured argument value

## Method: `public static ArgumentCaptor<U> forClass(Class<S> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static ArgumentCaptor<U> forClass(Class<S> clazz)", "entityFile": "ArgumentCaptor.java"} -->Build a new ArgumentCaptor.
        Note that an ArgumentCaptor *don't do any type checks*, it is only there to avoid casting
        in your code. This might however change (type checks could be added) in a
        future major release.
        @param clazz Type matching the parameter to be captured.
        @param <S> Type of clazz
        @param <U> Type of object captured by the newly built ArgumentCaptor
        @return A new ArgumentCaptor

## Class: `ArgumentCaptor`

        <!-- META {"entityType": "Class", "entitySignature": "ArgumentCaptor", "entityFile": "ArgumentCaptor.java"} -->Use it to capture argument values for further assertions.
        Mockito verifies argument values in natural java style: by using an equals() method.
        This is also the recommended way of matching arguments because it makes tests clean & simple.
        In some situations though, it is helpful to assert on certain arguments after the actual verification.
        For example:
        <pre class="code"><code class="java">
        ArgumentCaptor&lt;Person&gt; argument = ArgumentCaptor.forClass(Person.class);
        verify(mock).doSomething(argument.capture());
        assertEquals("John", argument.getValue().getName());
        Example of capturing varargs:
        <pre class="code"><code class="java">
        //capturing varargs:
        ArgumentCaptor&lt;Person&gt; varArgs = ArgumentCaptor.forClass(Person.class);
        verify(mock).varArgMethod(varArgs.capture());
        List expected = asList(new Person("John"), new Person("Jane"));
        assertEquals(expected, varArgs.getAllValues());
        Warning: it is recommended to use ArgumentCaptor with verification but not with stubbing.
        Using ArgumentCaptor with stubbing may decrease test readability because captor is created outside of assert (aka verify or 'then') block.
        Also it may reduce defect localization because if stubbed method was not called then no argument is captured.
        In a way ArgumentCaptor is related to custom argument matchers (see javadoc for ArgumentMatcher class).
        Both techniques can be used for making sure certain arguments where passed to mocks.
        However, ArgumentCaptor may be a better fit if:
        custom argument matcher is not likely to be reused
        you just need it to assert on argument values to complete verification
        Custom argument matchers via ArgumentMatcher are usually better for stubbing.
        This utility class *don't do any type checks*, the generic signatures are only there to avoid casting
        in your code.
        There is an annotation that you might find useful: &#64;Captor
        See the full documentation on Mockito in javadoc for Mockito class.
        @see Captor
        @since 1.8.0

# File: `ArgumentMatcher.java`

## Method: `public boolean matches(Object argument)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean matches(Object argument)", "entityFile": "ArgumentMatcher.java"} -->Informs if this matcher accepts the given argument.
        The method should never assert if the argument doesn't match. It
        should only return false.
        The argument is not using the generic type in order to force explicit casting in the implementation.
        This way it is easier to debug when incompatible arguments are passed to the matchers.
        You have to trust us on this one. If we used parametrized type then ClassCastException
        would be thrown in certain scenarios.
        For example:
        <pre class="code"><code class="java">
        //test, method accepts Collection argument and ArgumentMatcher&lt;List&gt; is used
        when(mock.useCollection(someListMatcher())).thenDoNothing();
        //production code, yields confusing ClassCastException
        //although Set extends Collection but is not compatible with ArgumentMatcher&lt;List&gt;
        mock.useCollection(new HashSet());
        See the example in the top level javadoc for ArgumentMatcher
        @param argument
        the argument
        @return true if this matcher accepts the given argument.

## Interface: `ArgumentMatcher`

        <!-- META {"entityType": "Interface", "entitySignature": "ArgumentMatcher", "entityFile": "ArgumentMatcher.java"} -->Allows creating customized argument matchers.
        This API was changed in Mockito 2.* in an effort to decouple Mockito from Hamcrest
        and reduce the risk of version incompatibility.
        Migration guide is included close to the bottom of this javadoc.
        For non-trivial method arguments used in stubbing or verification, you have following options
        (in no particular order):
        refactor the code so that the interactions with collaborators are easier to test with mocks.
        Perhaps it is possible to pass a different argument to the method so that mocking is easier?
        If stuff is hard to test it usually indicates the design could be better, so do refactor for testability!
        don't match the argument strictly, just use one of the lenient argument matchers like
        Mockito#notNull(). Some times it is better to have a simple test that works than
        a complicated test that seem to work.
        implement equals() method in the objects that are used as arguments to mocks.
        Mockito naturally uses equals() for argument matching.
        Many times, this is option is clean and simple.
        use ArgumentCaptor to capture the arguments and perform assertions on their state.
        Useful when you need to verify the arguments. Captor is not useful if you need argument matching for stubbing.
        Many times, this option leads to clean and readable tests with fine-grained validation of arguments.
        use customized argument matchers by implementing ArgumentMatcher interface
        and passing the implementation to the Mockito#argThat method.
        This option is useful if custom matcher is needed for stubbing and can be reused a lot.
        Note that Mockito#argThat demonstrates NullPointerException auto-unboxing caveat.
        use an instance of hamcrest matcher and pass it to
        org.mockito.hamcrest.MockitoHamcrest#argThat(org.hamcrest.Matcher)
        Useful if you already have a hamcrest matcher. Reuse and win!
        Note that org.mockito.hamcrest.MockitoHamcrest#argThat(org.hamcrest.Matcher) demonstrates NullPointerException auto-unboxing caveat.
        Implementations of this interface can be used with Matchers#argThat method.
        Use toString() method for description of the matcher
        - it is printed in verification errors.
        <pre class="code"><code class="java">
        class ListOfTwoElements implements ArgumentMatcher&lt;List&gt; {
        public boolean matches(Object list) {
        return ((List) list).size() == 2;
        }
        public String toString() {
        //printed in verification errors
        return "[list of 2 elements]";
        }
        }
        List mock = mock(List.class);
        when(mock.addAll(argThat(new ListOfTwoElements))).thenReturn(true);
        mock.addAll(Arrays.asList(&quot;one&quot;, &quot;two&quot;));
        verify(mock).addAll(argThat(new ListOfTwoElements()));
        To keep it readable you can extract method, e.g:
        <pre class="code"><code class="java">
        verify(mock).addAll(argThat(new ListOfTwoElements()));
        //becomes
        verify(mock).addAll(listOfTwoElements());
        Read more about other matchers in javadoc for Matchers class.
        2.0 migration guide
        All existing custom implementations of ArgumentMatcher will no longer compile.
        All locations where hamcrest matchers are passed to argThat() will no longer compile.
        There are 2 approaches to fix the problems:
        a) Refactor the hamcrest matcher to Mockito matcher:
        Use "implements ArgumentMatcher" instead of "extends ArgumentMatcher".
        Then refactor describeTo() method into toString() method.
        b) Use org.mockito.hamcrest.MockitoHamcrest.argThat() instead of Mockito.argThat().
        Ensure that there is <a href="http://hamcrest.org/JavaHamcrest/">hamcrest dependency on classpath
        (Mockito does not depend on hamcrest any more).
        What option is right for you? If you don't mind compile dependency to hamcrest
        then option b) is probably right for you.
        Your choice should not have big impact and is fully reversible -
        you can choose different option in future (and refactor the code)
        @param <T> type of argument
        @since 2.0

# File: `BDDMockito.java`

## Method: `BDDMyOngoingStubbing<T> willAnswer(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> willAnswer(Answer<?> answer)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#thenAnswer(Answer)
        @since 1.8.0

## Method: `BDDMyOngoingStubbing<T> will(Answer<?> answer)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> will(Answer<?> answer)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#then(Answer)
        @since 1.9.0

## Method: `BDDMyOngoingStubbing<T> willReturn(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> willReturn(T value)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#thenReturn(Object)
        @since 1.8.0

## Method: `BDDMyOngoingStubbing<T> willReturn(T value, T... values)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> willReturn(T value, T... values)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#thenReturn(Object, Object[])
        @since 1.8.0

## Method: `BDDMyOngoingStubbing<T> willThrow(Throwable... throwables)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> willThrow(Throwable... throwables)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#thenThrow(Throwable...)
        @since 1.8.0

## Method: `BDDMyOngoingStubbing<T> willThrow(Class<? extends Throwable> throwableType)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDMyOngoingStubbing<T> willThrow(Class<? extends Throwable> throwableType)", "entityFile": "BDDMockito.java"} -->See original OngoingStubbing#thenThrow(Class)
        @since 2.0.0

## Class: `BDDOngoingStubbingImpl`

        <!-- META {"entityType": "Class", "entitySignature": "BDDOngoingStubbingImpl", "entityFile": "BDDMockito.java"} -->@deprecated not part of the public API, use BDDMyOngoingStubbing instead.

## Method: `public static BDDMyOngoingStubbing<T> given(T methodCall)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDMyOngoingStubbing<T> given(T methodCall)", "entityFile": "BDDMockito.java"} -->see original Mockito#when(Object)
        @since 1.8.0

## Method: `public static Then<T> then(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Then<T> then(T mock)", "entityFile": "BDDMockito.java"} -->Bdd style verification of mock behavior.
        <pre class="code"><code class="java">
        person.ride(bike);
        person.ride(bike);
        then(person).should(times(2)).ride(bike);
        @see #verify(Object)
        @see #verify(Object, VerificationMode)
        @since 1.10.0

## Interface: `Then`

        <!-- META {"entityType": "Interface", "entitySignature": "Then", "entityFile": "BDDMockito.java"} -->Provides fluent way of mock verification.
        @param <T> type of the mock
        @since 1.10.5

## Class: `ThenImpl`

        <!-- META {"entityType": "Class", "entitySignature": "ThenImpl", "entityFile": "BDDMockito.java"} -->@deprecated not part of the public API, use Then instead.

## Method: `BDDStubber willAnswer(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willAnswer(Answer answer)", "entityFile": "BDDMockito.java"} -->See original Stubber#doAnswer(Answer)
        @since 1.8.0

## Method: `BDDStubber will(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber will(Answer answer)", "entityFile": "BDDMockito.java"} -->See original Stubber#doAnswer(Answer)
        @since 1.8.0

## Method: `BDDStubber willReturn(Object toBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willReturn(Object toBeReturned)", "entityFile": "BDDMockito.java"} -->See original Stubber#doReturn(Object)
        @since 2.0.0

## Method: `BDDStubber willReturn(Object toBeReturned, Object... nextToBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willReturn(Object toBeReturned, Object... nextToBeReturned)", "entityFile": "BDDMockito.java"} -->See original Stubber#doReturn(Object)
        @since 2.0.0

## Method: `BDDStubber willThrow(Throwable... toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willThrow(Throwable... toBeThrown)", "entityFile": "BDDMockito.java"} -->See original Stubber#doThrow(Throwable...)
        @since 1.8.0

## Method: `BDDStubber willThrow(Class<? extends Throwable> toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willThrow(Class<? extends Throwable> toBeThrown)", "entityFile": "BDDMockito.java"} -->See original Stubber#doThrow(Class)
        @since 2.0.0

## Method: `BDDStubber willThrow(Class<? extends Throwable> toBeThrown, Class<? extends Throwable>... nextToBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "BDDStubber willThrow(Class<? extends Throwable> toBeThrown, Class<? extends Throwable>... nextToBeThrown)", "entityFile": "BDDMockito.java"} -->See original Stubber#doThrow(Class, Class[])
        @since 2.0.0

## Method: `T given(T mock)`

        <!-- META {"entityType": "Method", "entitySignature": "T given(T mock)", "entityFile": "BDDMockito.java"} -->See original Stubber#when(Object)
        @since 1.8.0

## Class: `BDDStubberImpl`

        <!-- META {"entityType": "Class", "entitySignature": "BDDStubberImpl", "entityFile": "BDDMockito.java"} -->@deprecated not part of the public API, use BDDStubber instead.

## Method: `public static BDDStubber willThrow(Throwable... toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willThrow(Throwable... toBeThrown)", "entityFile": "BDDMockito.java"} -->see original Mockito#doThrow(Throwable[])
        @since 2.0.0

## Method: `public static BDDStubber willThrow(Class<? extends Throwable> toBeThrown)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willThrow(Class<? extends Throwable> toBeThrown)", "entityFile": "BDDMockito.java"} -->see original Mockito#doThrow(Class)
        @since 1.9.0

## Method: `public static BDDStubber willThrow(Class<? extends Throwable> toBeThrown, Class<? extends Throwable>... throwableTypes)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willThrow(Class<? extends Throwable> toBeThrown, Class<? extends Throwable>... throwableTypes)", "entityFile": "BDDMockito.java"} -->see original Mockito#doThrow(Class)
        @since 1.9.0

## Method: `public static BDDStubber willAnswer(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willAnswer(Answer answer)", "entityFile": "BDDMockito.java"} -->see original Mockito#doAnswer(Answer)
        @since 1.8.0

## Method: `public static BDDStubber will(Answer answer)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber will(Answer answer)", "entityFile": "BDDMockito.java"} -->see original Mockito#doAnswer(Answer)
        @since 2.0.0

## Method: `public static BDDStubber willReturn(Object toBeReturned)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willReturn(Object toBeReturned)", "entityFile": "BDDMockito.java"} -->see original Mockito#doReturn(Object)
        @since 1.8.0

## Method: `public static BDDStubber willReturn(Object toBeReturned, Object... toBeReturnedNext)`

        <!-- META {"entityType": "Method", "entitySignature": "public static BDDStubber willReturn(Object toBeReturned, Object... toBeReturnedNext)", "entityFile": "BDDMockito.java"} -->see original Mockito#doReturn(Object, Object...)
        @since 2.0.0

## Class: `BDDMockito`

        <!-- META {"entityType": "Class", "entitySignature": "BDDMockito", "entityFile": "BDDMockito.java"} -->Behavior Driven Development style of writing tests uses //given //when //then comments as fundamental parts of your test methods.
        This is exactly how we write our tests and we warmly encourage you to do so!
        Start learning about BDD here: <a href="http://en.wikipedia.org/wiki/Behavior_Driven_Development">http://en.wikipedia.org/wiki/Behavior_Driven_Development
        The problem is that current stubbing api with canonical role of when word does not integrate nicely with //given //when //then comments.
        It's because stubbing belongs to given component of the test and not to the when component of the test.
        Hence BDDMockito class introduces an alias so that you stub method calls with BDDMockito#given(Object) method.
        Now it really nicely integrates with the given component of a BDD style test!
        Here is how the test might look like:
        <pre class="code"><code class="java">
        import static org.mockito.BDDMockito.*;
        Seller seller = mock(Seller.class);
        Shop shop = new Shop(seller);
        public void shouldBuyBread() throws Exception {
        //given
        given(seller.askForBread()).willReturn(new Bread());
        //when
        Goods goods = shop.buyBread();
        //then
        assertThat(goods, containBread());
        }
        Stubbing voids with throwables:
        <pre class="code"><code class="java">
        //given
        willThrow(new RuntimeException("boo")).given(mock).foo();
        //when
        Result result = systemUnderTest.perform();
        //then
        assertEquals(failure, result);
        For BDD style mock verification take a look at Then in action:
        <pre class="code"><code class="java">
        person.ride(bike);
        person.ride(bike);
        then(person).should(times(2)).ride(bike);
        then(person).shouldHaveNoMoreInteractions();
        then(police).shouldHaveZeroInteractions();
        It is also possible to do BDD style InOrder verification:
        <pre class="code"><code class="java">
        InOrder inOrder = inOrder(person);
        person.drive(car);
        person.ride(bike);
        person.ride(bike);
        then(person).should(inOrder).drive(car);
        then(person).should(inOrder, times(2)).ride(bike);
        One of the purposes of BDDMockito is also to show how to tailor the mocking syntax to a different programming style.
        @since 1.8.0

# File: `Captor.java`

## Annotation: `Captor`

        <!-- META {"entityType": "Annotation", "entitySignature": "Captor", "entityFile": "Captor.java"} -->Allows shorthand org.mockito.ArgumentCaptor creation on fields.
        Example:
        <pre class="code"><code class="java">
        public class Test{
        &#64;Captor ArgumentCaptor&lt;AsyncCallback&lt;Foo&gt;&gt; captor;
        &#64;Before
        public void init(){
        MockitoAnnotations.initMocks(this);
        }
        &#64;Test public void shouldDoSomethingUseful() {
        //...
        verify(mock).doStuff(captor.capture());
        assertEquals("foo", captor.getValue());
        }
        }
        One of the advantages of using &#64;Captor annotation is that you can avoid warnings related capturing complex generic types.
        @see ArgumentCaptor
        @since 1.8.3

# File: `AnnotationEngine.java`

## Method: `Object createMockFor(Annotation annotation, Field field)`

        <!-- META {"entityType": "Method", "entitySignature": "Object createMockFor(Annotation annotation, Field field)", "entityFile": "AnnotationEngine.java"} -->@deprecated
        Please use AnnotationEngine#process(Class, Object) method instead that is more robust
        Creates mock, ArgumentCaptor or wraps field instance in spy object.
        Only if of correct annotation type.
        @param annotation Annotation
        @param field Field details

## Method: `void process(Class<?> clazz, Object testInstance)`

        <!-- META {"entityType": "Method", "entitySignature": "void process(Class<?> clazz, Object testInstance)", "entityFile": "AnnotationEngine.java"} -->Allows extending the interface to perform action on specific fields on the test class.
        See the implementation of this method to figure out what is it for.
        @param clazz Class where to extract field information, check implementation for details
        @param testInstance Test instance

## Interface: `AnnotationEngine`

        <!-- META {"entityType": "Interface", "entitySignature": "AnnotationEngine", "entityFile": "AnnotationEngine.java"} -->Configures mock creation logic behind @Mock, @Captor and @Spy annotations
        If you are interested then see implementations or source code of MockitoAnnotations#initMocks(Object)

# File: `DefaultMockitoConfiguration.java`

## Class: `DefaultMockitoConfiguration`

        <!-- META {"entityType": "Class", "entitySignature": "DefaultMockitoConfiguration", "entityFile": "DefaultMockitoConfiguration.java"} -->DefaultConfiguration of Mockito framework
        Currently it doesn't have many configuration options but it will probably change if future.
        See javadocs for IMockitoConfiguration on info how to configure Mockito

# File: `IMockitoConfiguration.java`

## Method: `Answer<Object> getDefaultAnswer()`

        <!-- META {"entityType": "Method", "entitySignature": "Answer<Object> getDefaultAnswer()", "entityFile": "IMockitoConfiguration.java"} -->Allows configuring the default answers of unstubbed invocations
        See javadoc for IMockitoConfiguration

## Method: `AnnotationEngine getAnnotationEngine()`

        <!-- META {"entityType": "Method", "entitySignature": "AnnotationEngine getAnnotationEngine()", "entityFile": "IMockitoConfiguration.java"} -->Configures annotations for mocks
        See javadoc for IMockitoConfiguration

## Method: `boolean cleansStackTrace()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean cleansStackTrace()", "entityFile": "IMockitoConfiguration.java"} -->This should be turned on unless you're a Mockito developer and you wish
        to have verbose (read: messy) stack traces that only few understand (eg:
        Mockito developers)
        See javadoc for IMockitoConfiguration
        @return if Mockito should clean stack traces

## Method: `boolean enableClassCache()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean enableClassCache()", "entityFile": "IMockitoConfiguration.java"} -->Allow objenesis to cache classes. If you're in an environment where classes
        are dynamically reloaded, you can disable this to avoid classcast exceptions.

## Interface: `IMockitoConfiguration`

        <!-- META {"entityType": "Interface", "entitySignature": "IMockitoConfiguration", "entityFile": "IMockitoConfiguration.java"} -->Use it to configure Mockito. For now there are not many configuration options but it may change in future.
        In most cases you don't really need to configure Mockito. For example in case of working with legacy code,
        when you might want to have different 'mocking style' this interface might be helpful.
        A reason of configuring Mockito might be if you disagree with the ReturnsEmptyValues unstubbed mocks return.
        To configure Mockito create exactly org.mockito.configuration.MockitoConfiguration class that implements this interface.
        Configuring Mockito is completely optional - nothing happens if there isn't any org.mockito.configuration.MockitoConfiguration on the classpath.
        org.mockito.configuration.MockitoConfiguration must implement IMockitoConfiguration or extend DefaultMockitoConfiguration
        Mockito will store single instance of org.mockito.configuration.MockitoConfiguration per thread (using ThreadLocal).
        For sanity of your tests, don't make the implementation stateful.
        If you have comments on Mockito configuration feature don't hesitate to write to mockito@googlegroups.com

# File: `MockitoAssertionError.java`

## Method: `public MockitoAssertionError(MockitoAssertionError error, String message)`

        <!-- META {"entityType": "Method", "entitySignature": "public MockitoAssertionError(MockitoAssertionError error, String message)", "entityFile": "MockitoAssertionError.java"} -->Creates a copy of the given assertion error with the custom failure message prepended.
        @param error The assertion error to copy
        @param message The custom message to prepend
        @since 2.0.0

# File: `MockitoException.java`

## Class: `MockitoException`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoException", "entityFile": "MockitoException.java"} --><!-- 91362de8-178a-11ea-8b50-333445793454 <=< ACCEPT -->Raised by mockito to emit an error either due to Mockito, or due to the User.
        The stack trace is filtered from mockito calls if you are using #getStackTrace().
        For debugging purpose though you can still access the full stacktrace using #getUnfilteredStackTrace().
        However note that other calls related to the stackTrace will refer to the filter stacktrace.<!-- ACCEPT >=> 91362de8-178a-11ea-8b50-333445793454 -->

# File: `MockitoSerializationIssue.java`

## Class: `MockitoSerializationIssue`

        <!-- META {"entityType": "Class", "entitySignature": "MockitoSerializationIssue", "entityFile": "MockitoSerializationIssue.java"} --><!-- 91362de8-178a-11ea-8b50-333445793454 <=< ACCEPT -->Raised by mockito to emit an error either due to Mockito, or due to the User.
        The stack trace is filtered from mockito calls if you are using #getStackTrace().
        For debugging purpose though you can still access the full stacktrace using #getUnfilteredStackTrace().
        However note that other calls related to the stackTrace will refer to the filter stacktrace.
        @since 1.10.0<!-- ACCEPT >=> 91362de8-178a-11ea-8b50-333445793454 -->

# File: `Discrepancy.java`

## Class: `Discrepancy`

        <!-- META {"entityType": "Class", "entitySignature": "Discrepancy", "entityFile": "Discrepancy.java"} -->@Deprecated. This class has been moved to internal packages because it was never meant to be public.
        If you need it for extending Mockito please let us know. You can still use org.mockito.internal.reporting.Discrepancy.
        However, the package clearly states that the class in a part of a public API so it can change.

